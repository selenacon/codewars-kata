def getChange(quantity):

    coinType = [5, 2, 1]
    coinNumber = []
    i = 0
    
    for coin in coinType:
        coinNumber.insert(i, quantity // coin)
        quantity %= coin
        if len(coinNumber) <3: i += 1
        else: return tuple(coinNumber)

# test cases
assert getChange(8) == (1, 1, 1)
assert getChange(5) == (1, 0, 0)
assert getChange(29) == (5, 2, 0)
assert getChange(0) == (0, 0, 0)