# Lists, tuples, dictionaries and sets
marks = [75, 45, 85, 60]
marks.append(90)
print("List:", marks)
print("First:", marks[0])

location = (6.9, 79.9)
latitude, longitude = location
print("Coordinates:", latitude, longitude)

students = {"Amal": 75, "Kamal": 45, "Nimal": 85}
students["Saman"] = 60

for name, score in students.items():
    print(name, score)

passed = {name: score for name, score in students.items() if score >= 50}
print("Passed:", passed)

categories = ["food", "travel", "food", "study"]
print("Unique categories:", set(categories))
