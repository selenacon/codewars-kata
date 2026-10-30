def comp(a, b):

    cuadrados = []

    if a != None and b != None:
        for numero in a:
            cuadrados.append(numero ** 2)
    return cuadrados.sort() == b.sort()

#test cases
if __name__ == '__main__':

    a = []
    b = []
    assert comp(a, b)
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a, b)
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a, b)
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a, b)
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    assert comp(a, b)