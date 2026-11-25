# 5. Files, Exceptions and Object-Oriented Basics

## Reading and writing text files
Use a context manager (`with`) so the file is closed reliably.
```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```
Modes include `r` (read), `w` (write/overwrite), `a` (append).

## Exceptions
Handle expected errors specifically.
```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a whole number.")
else:
    print("Age:", age)
```
Avoid broad `except:` blocks that hide programming errors.

Raise an exception when a function receives invalid input:
```python
def percentage(part, whole):
    if whole == 0:
        raise ValueError("whole must not be zero")
    return part / whole * 100
```

## Debugging
- Read the full traceback, especially the final exception line.
- Check variable values and types.
- Reduce the problem to a small reproducible example.
- Add tests for expected and edge cases.

## Object-oriented programming
A class defines a kind of object; an object is an instance of a class.
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def has_passed(self):
        return self.marks >= 50

student = Student("Amal", 75)
print(student.name)
print(student.has_passed())
```
- `__init__` initialises a new instance.
- `self` refers to the current instance.
- Attributes store data.
- Methods define behaviour.

Learn inheritance and composition after you are comfortable with classes. Do not force OOP into every small script.
