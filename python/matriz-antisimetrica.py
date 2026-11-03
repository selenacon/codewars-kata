
'''def esCuadrada(matriz):
     for fila in matriz:
        if len(fila) == len(matriz):
            return True
        else: return False'''


def esAntisimetrica(matriz):
    for fila in matriz:
        try:
            assert matriz[matriz.index(fila)][matriz.index(fila)] == matriz[matriz.index(fila)+1][matriz.index(fila)+1]
            assert len(fila) == len(matriz)
        except:
            return False
    i = 0
    k = 0
    while True:
        if matriz[i][round(k)] != -1 * matriz[round(k)][i]:
            return False
        elif k > len(matriz):
            break
        else:
            i+=1
            k+=1/len(matriz)
    return True
    

'''for fila in matriz:
        assert len(fila) == len(matriz)
        for columna in fila:
            else: return False
        return
    return'''
                

if __name__ == '__main__':
    assert esAntisimetrica([[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]) is True
''' matriz5 = [[1, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 1]]
    
    assert esAntisimetrica(matriz5) is False    
    
    assert esAntisimetrica([ [0, 1, 2],
                             [-1, 0, 3],
                             [-2, -3, 0]]) is True
    assert esAntisimetrica([ [0, 1, 2],
                             [-1, 0, -2],
                             [2, 2, 3]]) is False

    assert esAntisimetrica([ [1, 2, 5],
                             [0, 1, -9],
                             [0, 0, 1]]) is False
    
    assert esAntisimetrica([ [1, 2,  5],
                             [-2, 1, -9],
                             [-5, 0, 1]]) is False


    # casos test que no satisfacen la precondicion de que la matriz sea cuadrada:
    matriz5 = [[1, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 1]]

    assert esAntisimetrica(matriz5) is False

    matriz6 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert esAntisimetrica(matriz6) is False

    matriz7 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]

    assert esAntisimetrica(matriz7) is False


    # casos test matriz cuadrada:
    assert esMatrizCuadrada([[1, 0, 0, 0],
                            [0, 1, 1, 0],
                            [0, 0, 0, 1]]) is False

    assert esMatrizCuadrada([[1, 0, 0, 0, 0, 0, 0, 0, 0]]) is False

    assert esMatrizCuadrada([[1, 2, 3, 4],
                            [-2, 1, 5],
                            [-3, -5, 1, 1]]) is False

    assert esMatrizCuadrada([[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]) is True'''
