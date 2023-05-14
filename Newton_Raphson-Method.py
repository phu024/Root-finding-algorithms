# Define the function whose root we want to find
def func(x):
    return x**3 - 6*x*x + 11*x - 6

# Define the Newton-Raphson method function
def newton_rahpson(x, iteration, error):
    # Iterate through the maximum number of iterations specified
    for i in range(iteration):
        # Print the current iteration number, x value, and function value
        print(f"Iteration {i+1}: x = {x:.4f}, f(x) = {func(x):.4f}")
        
        # Check if the absolute value of the function value is less than the maximum error
        if abs(func(x)) < error:
            break
        
        # Calculate the next value of x using the Newton-Raphson method
        x = x - func(x) / (3*x*x - 12*x + 11)
    
    # Print the approximate root of the function
    print(f"The root is approximately {x:.4f}")

# Set the initial values of x, maximum number of iterations, and maximum error
x = 2.5
iteration = 100
error = 0.0001

# Call the Newton-Raphson method function with the specified arguments
newton_rahpson(x, iteration, error)
