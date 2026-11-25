# 1. Python Fundamentals

## What is Python?
Python is a high-level, general-purpose programming language. It is widely used in automation, data analysis, machine learning, web development and scientific computing.

## First program
```python
print("Hello, world!")
```
`print()` displays information in the output area.

## Comments
```python
# This is a single-line comment
```
Comments explain code to human readers and are ignored by Python.

## Variables
A variable is a name referring to an object/value.
```python
student_name = "Amal"
age = 21
height_m = 1.72
is_enrolled = True
```
Use descriptive names. Python convention is `snake_case`.

## Common built-in types
| Type | Example | Meaning |
|---|---|---|
| int | `42` | Integer |
| float | `3.14` | Floating-point number |
| str | `"Python"` | Text |
| bool | `True` | Boolean value |
| NoneType | `None` | Absence of a value |

Check a value's type:
```python
value = 42
print(type(value))
```

## Type conversion
```python
age_text = "21"
age_number = int(age_text)
price = float("125.50")
number_text = str(100)
```
Conversion can fail if the text is not valid for the requested type.

## Operators
- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `and`, `or`, `not`
- Assignment: `=`, `+=`, `-=`, `*=`

Remember:
- `=` assigns a value.
- `==` compares two values.
- `%` gives the remainder.
- `//` performs floor division.
- `**` raises to a power.

## Input and output
```python
name = input("Enter your name: ")
print("Hello,", name)
```
`input()` returns text (`str`). Convert numeric input before arithmetic:
```python
age = int(input("Enter age: "))
```

## Useful built-ins
`print()`, `input()`, `type()`, `len()`, `int()`, `float()`, `str()`, `sum()`, `min()`, `max()`, `round()`, `sorted()`.

## Common mistakes
- Using a variable before assigning it.
- Mixing strings and numbers without conversion.
- Confusing `=` with `==`.
- Misspelling variable names.
- Assuming `input()` automatically returns a number.
