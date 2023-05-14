## False Position Method to Find Root of Function

This Python script contains a function called `false_position` that implements the false position method to find the root of a given function `func`. The function `func` takes a single input `x` and returns the value of the function at that point. The false position method takes two initial guesses `a` and `b` for the root and uses linear interpolation to refine the guesses until the root is found within a given error tolerance.

### Usage

To use this function to find the root of a function `func`, simply call the `false_position` function with the following arguments:

```python
false_position(a, b, iteration, error)
```

- `a`: initial guess for the root
- `b`: initial guess for the root
- `iteration`: maximum number of iterations to perform
- `error`: the desired error tolerance for the root

### Example

In the provided example, the function `false_position` is used to find the root of the function defined in `func`. The initial guesses for the root are `a=2.5` and `b=4`, and the maximum number of iterations is set to `100` with an error tolerance of `0.0001`. The script will output the intermediate calculations and the approximate root found.

```python
lteration = 100
error = 0.0001
a = 2.5
b = 4
false_position(a, b, lteration, error)
```

### Output

The script will output the following for each iteration of the false position method:

- `Iteration i: a = a_i, b = b_i, c = c_i, f(c) = f(c_i)`: current values of `a`, `b`, `c`, and the value of the function at `c`
- `The root is approximately c`: the final approximation of the root found by the method

If `func(a)` and `func(b)` have the same sign, the function will return an error message and exit.

```python
Error: f(a) and f(b) have the same sign.
```