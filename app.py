import os
import json
from dotenv import load_dotenv
from brownie import network, accounts, Contract
from scripts.strategy import run_strategy, compound_fee
from brownie.network import gas_price
from brownie.network.gas.strategies import GasNowStrategy


FACTORY_ADRRESS = "0xBAD59D2BA9A532242F1287DeaBc4227E8150D074"      
ROUTER_ADDRESS = "0x34511BE0a5eB24183B077682cBec5c7a9C9c5ADb"            
VAULT_ADDRESS = "0xc10d2E42dE16719523aAA9277d1b9290aA6c3Ad5"


def init():
    load_dotenv()
    if network.show_active()!='mainnet':
        network.connect('mainnet')
    print(f'etherscan token is: {os.getenv("ETHERSCAN_TOKEN")}')
    sm_account = accounts.add(os.getenv("SM_PRIVATE_KEY"))
    vault_abi  =  json.load(open('./build/contracts/IVault.json', 'r'))['abi']
    vault_contract = Contract.from_abi(address = VAULT_ADDRESS, abi = vault_abi, name = 'Vault')
    router_abi = json.load(open('./build/contracts/IRouter.json', 'r'))['abi']
    router_contract = Contract.from_abi(address = ROUTER_ADDRESS, abi = router_abi, name = 'Router', owner=sm_account)
    POOL_ADDRESS = vault_contract.pool()
    pool_abi = json.load(open('./build/contracts/dependencies/Uniswap/uniswap-v3-core@1.0.0/IUniswapV3Pool.json', 'r'))['abi']
    pool_contract =  Contract.from_abi(address = POOL_ADDRESS, abi = pool_abi, name = 'Pool')
    gas_strategy = GasNowStrategy("standard")
    gas_price(gas_strategy)
    print(gas_strategy.get_gas_price(), sm_account.address)
    return router_contract, pool_contract

def lambda_handler(event, context):
    router_contract, pool_contract = init()
    if 'key' in event and event['key']=='14 day':
        run_strategy(pool_contract, router_contract, range_percent=30)
    else:
        compound_fee(router_contract, VAULT_ADDRESS)