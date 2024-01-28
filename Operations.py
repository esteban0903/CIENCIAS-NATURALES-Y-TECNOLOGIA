import math


def addition(a, b):
    pr = round(a[0] + b[0], 2)
    pi = round(a[1] + b[1], 2)
    return pr, pi


def multiplication(a, b):
    pr = round(a[0]*b[0]-a[1]*b[1], 2)
    pi = round(a[0]*b[1]+b[0]*a[1], 2)
    return pr, pi


def subtraction(a, b):
    pr = round(a[0] - b[0], 2)
    pi = round(a[1] - b[1], 2)
    return pr, pi


def division(a, b):
    denominator = b[0]**2 + b[1]**2
    if denominator == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    pr = round((a[0]*b[0] + a[1]*b[1]) / denominator, 2)
    pi = round((b[0]*a[1] - a[0]*b[1]) / denominator, 2)
    return pr, pi


def modulus(a):
    num = round((a[0]**2 + a[1]**2)**0.5, 2)
    return num


def conjugate(a):
    return round(a[0], 2), round(a[1] * -1, 2)


def phase(a):
    if a[1] == 0:
        if a[0] > 0:
            angle = 0
        elif a[0] < 0:
            angle = math.pi
        else:
            raise ZeroDivisionError("Division by zero is not allowed")
    elif a[0] == 0:
        angle = math.pi/2 if a[1] > 0 else -math.pi/2
    else:
        angle = round(math.atan(a[0]/a[1]), 2)
    return angle


def cartesian_polar(a):
    ρ = round(modulus(a), 2)
    θ = round(phase(a), 2)
    pr = round(ρ*math.cos(θ), 2)
    pi = round(ρ*math.sin(θ), 2)
    return pr, pi


def polar_cartesian(a):
    pr = round(a[0]*math.cos(a[1]), 2)
    pi = round(a[0]*math.sin(a[1]), 2)
    return pr, pi
