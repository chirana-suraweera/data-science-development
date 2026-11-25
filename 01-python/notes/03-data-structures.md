# 3. Python Data Structures

## Lists
Ordered, mutable collections. Duplicates are allowed.
```python
marks = [75, 45, 85, 60]
print(marks[0])      # first item
print(marks[-1])     # last item
marks.append(90)
marks[1] = 50
```
Useful methods: `append`, `extend`, `insert`, `remove`, `pop`, `sort`, `reverse`, `index`, `count`.

Slicing:
```python
marks[1:3]   # indices 1 and 2
marks[:2]    # beginning to index 1
marks[2:]    # index 2 to end
marks[::-1]  # reversed copy
```

## Tuples
Ordered, immutable collections.
```python
coordinates = (6.9, 79.9)
latitude, longitude = coordinates
```
Useful when a fixed group of values should not be changed.

## Dictionaries
Mappings of unique keys to values.
```python
student_marks = {"Amal": 75, "Kamal": 45}
print(student_marks["Amal"])
student_marks["Nimal"] = 85
student_marks["Amal"] = 80
```
Useful methods:
- `.keys()` — keys
- `.values()` — values
- `.items()` — key-value pairs
- `.get(key, default)` — safe lookup
- `.update(other)` — add/update entries
- `.pop(key)` — remove and return an entry

Iterate over key-value pairs:
```python
for name, marks in student_marks.items():
    print(name, marks)
```

## Sets
Unordered collections of unique elements.
```python
unique_categories = {"food", "travel", "food"}
print(unique_categories)  # one "food" entry
```
Useful operations: union `|`, intersection `&`, difference `-`.

## Choosing a structure
| Need | Choose |
|---|---|
| Ordered sequence that may change | List |
| Fixed sequence | Tuple |
| Lookup by a meaningful key | Dictionary |
| Unique values and membership tests | Set |

## Mutability
Lists, dictionaries and sets are mutable. Strings and tuples are immutable. Understand this distinction when passing objects to functions or sharing references.

## Common mistakes
- Accessing a missing dictionary key directly.
- Using an out-of-range list index.
- Assuming sets preserve a meaningful positional order.
- Modifying a collection while iterating over it without care.
