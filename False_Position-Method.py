def func(x):
    # Define the function to be evaluated
    return x**3 - 6*x*x + 11*x - 6

def false_position(a, b, iteration, error):
    if func(a) * func(b) >= 0:
        # Check if the function has the same sign at the endpoints
        # If true, the algorithm won't work since there won't be any root
        print("Error: f(a) and f(b) have the same sign.")
        return

    for i in range(iteration):
        # Calculate the next approximation of the root using false position method
        c = a - func(a) * (b - a) / (func(b) - func(a))
        print(f"Iteration {i+1}: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, f(c) = {func(c):.4f}")
        if abs(b - a) < error:
            # Check if the error is within tolerance
            break
        if func(c) == 0:
            # Check if c is exactly the root
            break
        
        if func(c) * func(b) < 0:
            # Update the interval based on the sign of f(c)
            a = c
        else:
            b = c
    print(f"The root is approximately {c:.4f}")

# Set the parameters for the algorithm
iteration = 100
error = 0.0001
a = 2.5
b = 4

# Call the false position method with the given parameters
false_position(a, b, iteration, error)
