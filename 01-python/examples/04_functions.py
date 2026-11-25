# Functions and return values
def calculate_average(values):
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def classify_score(score, pass_mark=50):
    return "Pass" if score >= pass_mark else "Fail"


scores = [70, 80, 90]
average = calculate_average(scores)

print("Average:", average)
print("Status:", classify_score(average))
