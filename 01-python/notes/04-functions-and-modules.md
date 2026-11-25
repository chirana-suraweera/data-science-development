# 4. Functions, Scope and Modules

## Defining a function
A function packages reusable logic.
```python
def calculate_average(values):
    return sum(values) / len(values)

scores = [70, 80, 90]
average = calculate_average(scores)
print(average)
```

## Parameters and arguments
- Parameter: name in the function definition.
- Argument: value supplied when calling the function.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Amal"))
print(greet("Nimal", greeting="Welcome"))
```

## return versus print
- `print()` displays a value.
- `return` sends a result back to the caller and ends that function call.
A returned value does not have to be assigned to a variable; it can be passed directly to another function.

## Validation
```python
def safe_average(values):
    if len(values) == 0:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)
```

## Scope
Variables created inside a function are generally local to that function. Pass required values as arguments and return results rather than relying on global variables.

## Modules
A module is a Python file that can be imported.
```python
import math
print(math.sqrt(25))

from statistics import mean
print(mean([2, 4, 6]))
```
Use imports at the top of a file and avoid naming your own files after standard-library modules (for example, do not name a file `statistics.py` if you import `statistics`).

## Comprehensions
```python
squares = [number ** 2 for number in range(5)]
even_squares = [number ** 2 for number in range(10) if number % 2 == 0]
```
Prefer readable code over overly complicated one-line expressions.

## Common mistakes
- Forgetting to return a value.
- Returning inside a loop unintentionally.
- Confusing parameters and arguments.
- Writing functions that depend on hidden global state.
