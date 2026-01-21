#!/usr/bin/python3
"""
A function that multiplies 2 matrices by using the module NumPy
"""


def lazy_matrix_mul(m_a, m_b):
    import numpy as np
    return np.matmul(m_a, m_b)
