def newton_raphson(f, f_der, x0, tolerance=1e-6, max_iterations=100):
    x = x0
    for i in range(max_iterations):
        f_val = f(x)
        if abs(f_val) < tolerance:
            return x, i
        f_der_val = f_der(x)
        if f_der_val == 0:
            return None
        x -= f_val / f_der_val
    return None

# Prompt the user for the function, its derivative, and the initial guess for the root
f_str = input("Enter the function f(x): ")
f_der_str = input("Enter the derivative of f(x): ")
x0 = float(input("Enter the initial guess for the root: "))

# Define the function and its derivative as lambda functions
f = lambda x: eval(f_str)
f_der = lambda x: eval(f_der_str)

# Find the root using the Newton-Raphson method
root, iterations = newton_raphson(f, f_der, x0)
if root is not None:
    print(f"Root found: {root:.6f} after {iterations} iterations.")
else:
    print("Root not found.")
