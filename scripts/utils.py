import numpy as np


def get_price(tick, decimals_diff):
    return (10**decimals_diff)/1.0001**tick

def get_tick(price, decimals_diff, tick_spacing):
    tick =  int(np.log(10**decimals_diff/price)/np.log(1.0001))
    return int(tick/tick_spacing)*tick_spacing