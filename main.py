from math import e, sin, cos, log10, tan

def f(x):
    return eval(fx)  # evaluate the user input as a Python expression

def df(x):
    h = 1e-6  # small step size
    return (f(x + h) - f(x)) / h  # approximate the derivative using a finite difference

def newton_raphson(x0, tols):
    """
    x0: initial guess
    eps: tolerance
    """
    xn = x0
    while True:
        fxn = f(xn)
        if abs(fxn) < tols:
            return xn
        Dfxn = df(xn)
        if Dfxn == 0:
            return None
        xn = xn - fxn/Dfxn

# main program
fx = input("Enter f(x): ")
x0 = float(input("Enter initial guess: "))
tols = 1e-6
# tols = float(input("Enter tolerance: "))
dec = int(input("Enter number of decimal upto which you need solution to be correct: "))
root = newton_raphson(x0, tols)
round_root = round(root, dec)
if root is not None:
    print("Root: ", round_root)
else:
    print("No root found")
