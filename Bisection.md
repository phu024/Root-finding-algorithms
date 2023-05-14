# Bisection Method to Find Root of a Function

This Python script implements the bisection method to find the root of a given function. The bisection method is a simple and robust numerical method for finding roots of a function.

## Function
The function `func(x)` defined in the code returns the value of a polynomial function `x**3 - 6*x*x + 11*x - 6`.

## Bisection Method
The `bisection()` function implements the bisection method to find the root of the `func()` function between the given interval `[a,b]`. The `iteration` argument specifies the maximum number of iterations allowed and the `error` argument specifies the tolerance level for the approximate root.

The algorithm checks if `func(a)` and `func(b)` have opposite signs, which ensures that the root lies between `a` and `b`. If not, an error message is displayed.

The algorithm then starts iterating until the approximate root is found within the specified tolerance level or the maximum number of iterations is reached. At each iteration, the midpoint of the interval `[a,b]` is computed and the value of the function at the midpoint `c` is evaluated. Depending on the sign of `func(c)` and `func(b)`, the interval is updated accordingly. The process is repeated until the approximate root is found.

The script outputs the iteration number, interval endpoints `a` and `b`, midpoint `c`, and function value at `c` for each iteration. Finally, it displays the approximate root of the function within the specified tolerance level.

## Usage
To use the script, set the initial interval `[a,b]`, maximum number of iterations `iteration`, and the tolerance level `error` as desired. Then, call the `bisection()` function with these arguments.

## Example
In the provided code, the bisection method is applied to find the root of the function `x**3 - 6*x*x + 11*x - 6` in the interval `[2.5, 4]` with a maximum of 100 iterations and a tolerance level of 0.0001. The script displays the iteration number, interval endpoints `a` and `b`, midpoint `c`, and function value at `c` for each iteration. Finally, it displays the approximate root of the function within the specified tolerance level.

```python
a = 2.5
b = 4
iteration = 100
error = 0.0001
bisection(a, b, iteration, error)
```