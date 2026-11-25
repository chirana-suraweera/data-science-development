# Basic class and object
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def has_passed(self):
        return self.marks >= 50

    def display(self):
        print(f"{self.name}: {self.marks} — "
              f"{'Pass' if self.has_passed() else 'Fail'}")


students = [
    Student("Amal", 75),
    Student("Kamal", 45),
]

for student in students:
    student.display()
