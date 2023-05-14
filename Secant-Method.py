# Define the function we want to find the root of
def func(x):
    return x**3 - 6*x*x + 11*x - 6

# Implement the Secant method for finding the root
def secant(a, b, iteration, error):
    for i in range(iteration):
        # Print the current estimates of the root and function values
        print(f"Iteration {i+1}: a = {a:.4f}, b = {b:.4f}, f(a) = {func(a):.4f}, f(b) = {func(b):.4f}")
        # Check if the error is below the specified tolerance
        if abs(func(b)) < error:
            break
        # Update the estimates of the root based on the Secant method formula
        c = b - func(b) * (b - a) / (func(b) - func(a))
        a = b
        b = c
    
    # Print the final estimate of the root
    print(f"The root is approximately {b:.4f}")

# Set the initial parameters for the Secant method
iteration = 100
error = 0.0001
a = 2.5
b = 0

# Call the Secant method function with the specified parameters
secant(a, b, iteration, error)
