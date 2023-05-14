# Define the function we want to find the root of
def func(x):
    return x**3 - 6*x*x + 11*x - 6

# Define the bisection method to find the root of a function within an interval
def bisection(a, b, iteration, error):
    # Check if the interval is valid
    if func(a) * func(b) >= 0:
        print("Error: f(a) and f(b) have the same sign.")
        return
    
    # Iterate until the desired accuracy is achieved or the maximum number of iterations is reached
    for i in range(iteration):
        # Calculate the midpoint of the interval
        c = (a + b) / 2
        # Print the current iteration information
        print(f"Iteration {i+1}: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, f(c) = {func(c):.4f}")
        # Check if the current approximation is accurate enough
        if abs(b - a) < error:
            break
        # Check if the midpoint is the root
        if func(c) == 0:
            break
        # Update the interval based on the sign of the function at the midpoint
        elif func(c) * func(b) < 0:
            a = c
            print("True")
        else:
            b = c
            print("False")
    
    # Print the final approximation of the root
    print(f"The root is approximately {c:.4f}")

# Set the initial values for the interval, maximum number of iterations, and desired accuracy
a = 2.5
b = 4
iteration = 100
error = 0.0001

# Call the bisection method with the specified inputs
bisection(a, b, iteration, error)
