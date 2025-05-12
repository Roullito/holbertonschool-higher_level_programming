#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for ligne in matrix:
        new_ligne = []
        for value in ligne:
            new_ligne.append(value ** 2)
        result.append(new_ligne)
    return result
