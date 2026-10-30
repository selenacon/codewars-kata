'''
Welcome young Jedi!

In this Kata, you must create a function that takes an amount of US currency in cents, 
and returns a dictionary/hash which shows the least amount of coins used to make up that amount.

The only coin denominations considered in this exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢).

Therefore, the dictionary returned should contain exactly 4 key/value pairs.

Notes:

If the function is passed either 0 or a negative number, the function should return the dictionary with all values equal to 0.
If a float is passed into the function, its value should be rounded down, and the resulting dictionary should never contain fractions of a coin.
'''

def loose_change(cents):

    coinType = [25, 10, 5, 1]
    coinNumber = []
    
    while len(coinNumber) <4:
        for coin in coinType:
            coinNumber.insert(coinType.index(coin), cents // coin)
            cents %= coin
    return coinNumber #todo: convert to dictionary
    

# test cases
'''assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
assert loose_change(0) ==  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}'''

print(loose_change(29))