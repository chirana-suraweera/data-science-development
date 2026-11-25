# 2. Conditional Statements and Loops

## Conditional statements
Use conditions to choose which code runs.
```python
score = 72

if score >= 75:
    grade = "A"
elif score >= 65:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "Fail"

print(grade)
```
Python uses indentation to define code blocks. Be consistent; four spaces is conventional.

## Boolean conditions
A comparison evaluates to `True` or `False`.
```python
age >= 18
score >= 50 and attendance >= 80
is_registered or has_guest_pass
not is_suspended
```

## for loops
Use a `for` loop to iterate over an iterable:
```python
for number in [2, 4, 6]:
    print(number)
```
`range(start, stop, step)` generates a sequence of integers; the stop value is excluded.
```python
for i in range(1, 6):
    print(i)
```

## while loops
Repeat while a condition remains true:
```python
count = 0
while count < 3:
    print(count)
    count += 1
```
Make sure the loop condition can eventually become false.

## break and continue
- `break` exits the nearest loop.
- `continue` skips to the next iteration.

## Accumulation and filtering
```python
values = [3, 8, 10, 5]
total = 0
for value in values:
    total += value

even_values = []
for value in values:
    if value % 2 == 0:
        even_values.append(value)
```

## Common mistakes
- Incorrect indentation.
- Off-by-one errors with `range()`.
- Infinite `while` loops.
- Using `=` instead of `==` in a condition.
- Forgetting to initialise an accumulator before a loop.
