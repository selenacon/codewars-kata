def change(quantity):
    coinType = [5, 2, 1]
    coinNumber = [0, 0, 0]
    i = 0
    for coin in coinType:
        coinNumber.insert(i, quantity // coin)
        quantity = quantity % coin
        if quantity !=0: i += 1
        else: return coinNumber[:3]
print(change(8)) #(1, 1, 1)
print(change(5)) #(1, 0, 0)
print(change(29)) #(5, 2, 0)
print(change(0)) #(0, 0, 0)