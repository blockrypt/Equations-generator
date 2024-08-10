import math

def solve_quadratic_equation(a, b, c):
    """Решает квадратное уравнение вида ax^2 + bx + c = 0 и возвращает округленные до двух знаков корни x1 и x2 в виде строки, разделённой запятыми."""
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"{round(x1, 2)},{round(x2, 2)}"
    elif discriminant == 0:
        x = -b / (2 * a)
        return f"{round(x, 2)}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        x1 = f"{round(real_part, 2)}+{round(imaginary_part, 2)}i"
        x2 = f"{round(real_part, 2)}-{round(imaginary_part, 2)}i"
        return f"{x1}, {x2}"
