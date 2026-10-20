def permute_a_palindrome(input):
    charCount = ''.join(set(input))
    for x in input:
        if len(input) % 2 == 0:
            return input.count(charCount) %2 == 0
print(permute_a_palindrome('abbc')) #UNFINISHED