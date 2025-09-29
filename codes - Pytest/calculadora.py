def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def potencia(a, b):
    return a ** b