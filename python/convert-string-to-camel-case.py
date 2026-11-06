def to_camel_case(text):
    import re
#    return ''.join([word[0].swapcase() for word in text.replace('-''_', ' ') if word[0].lower()])
    print(re.split(r'-'r'_','1-2-3_4_5'))

#test cases
if __name__ == '__main__':
    assert to_camel_case("") == ""
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"