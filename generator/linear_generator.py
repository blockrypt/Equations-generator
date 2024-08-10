import random

def generate_linear_equation():
    """Генерирует линейное уравнение вида ax + b = 0 с ограниченными коэффициентами и возвращает коэффициенты a и b."""
    a = random.randint(-5, 5)
    while a == 0:
        a = random.randint(-5, 5)
    b = random.randint(-10, 10)
    return a, b
