#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """multiply matrices
    Args:
        m_a: matrix a
        m_b: matrix b

    Return: multiplication of a and b
    """
    if all(isinstance(row, list) for row in m_a) is False:
        raise TypeError('m_a must be a list')
    if all(isinstance(row, list) for row in m_b) is False:
        raise TypeError('m_b must be a list')
    if m_a == []:
        raise ValueError('m_a can\'t be empty')
    if m_b == []:
        raise ValueError('m_b can\'t be empty')
    if all(isinstance(elem, (int, float)) for row in m_a for elem in row) is False:
        raise TypeError('m_a should contain only integers or floats')
    if all(isinstance(elem, (int, float)) for row in m_b for elem in row) is False:
        raise TypeError('m_b should contain only integers or floats')
    a = len(m_a[0])
    b = len(m_b[0])
    for row in m_a:
        if len(row) is not a:
            raise TypeError('each row of m_a must should be of the same size')
    for row in m_b:
        if len(row) is not b:
            raise TypeError('each row of m_b must should be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')
    result = [[sum(x * y for x, y in zip(m_a_row, m_b_col))
                   for m_b_col in zip(*m_b)] for m_a_row in m_a]
    return(result)
