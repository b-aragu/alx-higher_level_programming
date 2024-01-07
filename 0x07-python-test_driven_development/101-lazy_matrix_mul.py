#!/usr/bin/python3

"""multiplies 2 matrix using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        a function that multiplies a 2 matrices

        Args:
            m_a (list of lists of ints/float): the first matrix
            m_b (list of lists of ints/float): the second matrix
    """
    return (np.matmul(m_a, m_b))
