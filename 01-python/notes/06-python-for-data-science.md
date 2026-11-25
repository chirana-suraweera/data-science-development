# 6. Python for Data Science — Bridge to the Next Module

This note introduces the Python concepts that will be used heavily in data analysis. Detailed NumPy and Pandas learning belongs in `03-data-analysis/`.

## Why Python is useful in data science
Python provides general-purpose programming plus a large ecosystem for numerical computing, data manipulation, visualisation, machine learning and automation.

## Core libraries to recognise
- NumPy: numerical arrays and vectorised computation.
- Pandas: labelled tabular data using Series and DataFrames.
- Matplotlib: plotting and visualisation.
- Seaborn: statistical visualisation built on Matplotlib.
- Scikit-learn: machine-learning tools.

## Example: calculate simple descriptive values
```python
temperatures = [29.5, 30.0, 28.5, 31.0, 29.0]

average = sum(temperatures) / len(temperatures)
minimum = min(temperatures)
maximum = max(temperatures)

print("Average:", round(average, 2))
print("Minimum:", minimum)
print("Maximum:", maximum)
```

## Why NumPy and Pandas come next
Plain Python lists are useful, but data work often involves large tables, missing values, filtering, grouping, joining and numerical operations. NumPy and Pandas provide specialised structures and operations for these tasks.

## Readiness checklist
- [ ] I can write a function that accepts a list and returns a result.
- [ ] I can filter a list using a condition.
- [ ] I can loop through dictionary key-value pairs.
- [ ] I can read a text file and handle a missing-file error.
- [ ] I can explain the difference between a list and a dictionary.
- [ ] I can explain `return` versus `print`.
