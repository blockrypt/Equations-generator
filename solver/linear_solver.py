def solve_linear_equation(a, b):
    """Решает линейное уравнение вида ax + b = 0 и возвращает округленный до двух знаков корень x."""
    x = -b / a
    return round(x, 2)
