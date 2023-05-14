

## Secant Method for Finding the Root of a Function

This code implements the Secant method for finding the root of a function, which is a numerical method that uses an iterative process to approximate the root of a function. The Secant method is similar to the Newton-Raphson method, but instead of using the derivative of the function, it uses an approximation of the derivative.

The code defines the function `func(x)` that we want to find the root of. In this case, the function is `x**3 - 6*x*x + 11*x - 6`. This function can be changed to any function for which we want to find the root.

The code also defines the `secant(a, b, iteration, error)` function that implements the Secant method. This function takes four parameters:
- `a`: The initial estimate of the root.
- `b`: Another initial estimate of the root, which should be close to `a`.
- `iteration`: The maximum number of iterations that the Secant method will perform.
- `error`: The desired tolerance for the error between the estimated root and the true root.

The Secant method is an iterative process that updates the estimates of the root in each iteration based on the Secant method formula. The function prints the current estimates of the root and function values in each iteration, and stops iterating when the error is below the specified tolerance.

Finally, the code sets the initial parameters for the Secant method (`iteration`, `error`, `a`, and `b`), and calls the `secant` function with these parameters to find the root of the function `func(x)`.

To use this code for finding the root of a different function, simply replace the `func(x)` function definition with the desired function, and update the initial parameters for the Secant method as necessary.