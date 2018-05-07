#!/usr/bin/python3


def lazy_matrix_mul(m_a, m_b):
    """multiply matrices
    Args:
        m_a: matrix a
        m_b: matrix b

    Return: multiplication of a and b
    """
    import numpy

    result = numpy.dot(m_a, m_b)

    return(result)
