def add(a, b):
    """add function"""
    return a + b
def sub(a, b):
    """sub function"""
    return a - b
def mul(a, b):
    """mul function"""
    return a * b
def div(a, b):
    """div function"""
    if b == 0:
        raise ZeroDivisionError
    return a / b
