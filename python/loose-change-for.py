def getChange(quantity):

    coinType = [5, 2, 1]
    coinNumber = []
    
    for coin in coinType:
        coinNumber.insert(coinType.index(coin), quantity // coin)
        quantity %= coin
    return tuple(coinNumber)

# test cases
assert getChange(8) == (1, 1, 1)
assert getChange(5) == (1, 0, 0)
assert getChange(29) == (5, 2, 0)
assert getChange(0) == (0, 0, 0)