

## Newton-Raphson Method for Finding Roots

This code implements the Newton-Raphson method to find the root of a given function `func(x)`. The method uses an initial guess `x` and iteratively improves it until the value of the function at the guess is close enough to zero, as determined by the `error` parameter.

The function `newton_rahpson` takes three arguments:
- `x`: The initial guess for the root.
- `iteration`: The maximum number of iterations allowed.
- `error`: The maximum allowable error.

The code prints the current iteration number, the current guess `x`, and the value of the function at `x`. It stops the iteration when either the maximum number of iterations is reached or the value of the function at the current guess is within the specified error.

At the end of the iteration, the code prints the approximate root that was found.

## Example Usage

To use this code, simply call the `newton_rahpson` function with the desired initial guess, maximum number of iterations, and maximum allowable error. For example:

```
newton_rahpson(2.5, 100, 0.0001)
```

This will find the root of the function `func(x) = x**3 - 6*x*x + 11*x - 6` starting from an initial guess of `x = 2.5`, allowing up to `100` iterations and requiring that the error be less than `0.0001`.

Note that the code can be modified to work with different functions by simply changing the implementation of the `func(x)` function.