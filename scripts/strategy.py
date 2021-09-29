from scripts.utils import get_price, get_tick
from brownie.network.gas.strategies import GasNowStrategy

# function to run the strategy
def run_strategy(pool_contract, router_contract, range_percent):
    decimals_diff = 12
    out = pool_contract.slot0()
    start_price = get_price(out[1], decimals_diff)
    lower_price = start_price*(1-range_percent/100)
    upper_price = start_price/1.0001
    tick_spacing = pool_contract.tickSpacing()
    lower_tick, upper_tick = get_tick(lower_price, decimals_diff, tick_spacing), get_tick(upper_price, decimals_diff, tick_spacing)
    if lower_tick > upper_tick:
        lower_tick, upper_tick = upper_tick, lower_tick
    print(lower_tick, upper_tick)
    txn = router_contract.newLimitLiquidity(lower_tick, upper_tick, 100, True, {"allow_revert":True, "gas_limit": 4000000})  
    print(txn.info())      

def compound_fee(router_contract, vault_address):
    txn = router_contract.compoundFee(vault_address, {"allow_revert":True, "gas_limit": 2000000})
    print(txn.info())




