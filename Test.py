def bisection(func, a, b, max_iter, error):
    if func(a) * func(b) >= 0:
        print("Error: f(a) and f(b) have the same sign.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        print(f"Iteration {i+1}: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, f(c) = {func(c):.4f}")
        if abs(func(c)) < error:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    print(f"The root is approximately {c:.4f}")


def newton_raphson(func, x, max_iter, error):
    for i in range(max_iter):
        print(f"Iteration {i+1}: x = {x:.4f}, f(x) = {func(x):.4f}")
        if abs(func(x)) < error:
            break
        x = x - func(x) / derivative(func, x, dx=1e-6)
    print(f"The root is approximately {x:.4f}")


def derivative(func, x, dx=1e-6):
    return (func(x + dx) - func(x)) / dx


def secant(func, a, b, max_iter, error):
    for i in range(max_iter):
        print(f"Iteration {i+1}: a = {a:.4f}, b = {b:.4f}, f(a) = {func(a):.4f}, f(b) = {func(b):.4f}")
        if abs(func(b)) < error:
            break
        c = b - func(b) * (b - a) / (func(b) - func(a))
        a = b
        b = c
    print(f"The root is approximately {b:.4f}")


def false_position(func, a, b, max_iter, error):
    if func(a) * func(b) >= 0:
        print("Error: f(a) and f(b) have the same sign.")
        return None

    for i in range(max_iter):
        c = a - func(a) * (b - a) / (func(b) - func(a))
        print(f"Iteration {i+1}: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, f(c) = {func(c):.4f}")
        if abs(b - a) < error:
            break
        if func(c) == 0:
            break
        if func(c) * func(b) < 0:
            a = c
        else:
            b = c
    print(f"The root is approximately {c:.4f}")

def test_algorithms():
    func = lambda x: x**3 - 6*x**2 + 11*x - 6
    
    print("Bisection method:")
    bisection(func, 0, 3, 10, 1e-6)
    
    print("\nNewton-Raphson method:")
    newton_raphson(func, 2, 10, 1e-6)
    
    print("\nSecant method:")
    secant(func, 0, 3, 10, 1e-6)
    
    print("\nFalse position method:")
    false_position(func, 0, 3, 10, 1e-6)


if __name__ == "__main__":
    test_algorithms()
