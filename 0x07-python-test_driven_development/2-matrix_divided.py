#!/usr/bin/python3
"""
this module provide function divide elements of a matrix.
arg a matrix and a integer div.
"""

def matrix_divided(matrix, div):
    """
    matrix_divide: divide elements of matrix by int

    :param matrix: elements are divided.
    :param div:  int to divide the matrix.

    Raise:
            TypeError: div not int or float
            TypeError: matix is not a list of list of number
            ZeroDivisionError: Div is 0
            
    :return:  divided list
    """
    if matrix is None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    Divided_List =[]
    Matrix_Len = len(matrix[0])

    if not isinstance(div,(int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:

        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        list = []
        if len(i) != Matrix_Len:
            raise TypeError("Each row of the matrix must have the same size")

        for j in i:
            if not isinstance(j, (int,float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            List = list.append(round(j / div, 2))
        Divided_List.append(list)

    return Divided_List
