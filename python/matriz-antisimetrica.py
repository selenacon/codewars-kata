'''def esMatrizCuadrada(matriz):
    numeroFilas = len(matriz)
    for fila in matriz:
        return len(fila) == numeroFilas'''

def esAntisimetrica(matriz):
    for fila in matriz:
        if len(fila) == len(matriz):
            return matriz[matriz.index(fila)] == matriz[(matriz.index(fila)+1)]
        else: pass
    return False
        '''while matriz[matriz.index(fila)] == matriz[(matriz.index(fila)+1)]:
            index = 0
            return matriz.count(matriz[fila[index]][index]) < 2'''
                

if __name__ == '__main__':
    matriz5 = [[1, 0, 0, 0],
                   [0, 1, 1, 0],
                   [0, 0, 0, 1]]
    
    assert esAntisimetrica(matriz5) is False    
'''    assert esAntisimetrica([[0, 0, 0],
                                 [0, 0, 0],
                                 [0, 0, 0]]) is True
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
