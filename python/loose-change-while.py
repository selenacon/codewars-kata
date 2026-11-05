def getChange(quantity):

    coinType = [5, 2, 1]
    coinNumber = []
    while len(coinNumber) <3:
        index = len(coinNumber)
        coinNumber.append(quantity // coinType[index])
        quantity %= coinType[index]
    return tuple(coinNumber)
    
# test cases
assert getChange(8) == (1, 1, 1)
assert getChange(5) == (1, 0, 0)
assert getChange(29) == (5, 2, 0)
assert getChange(0) == (0, 0, 0)