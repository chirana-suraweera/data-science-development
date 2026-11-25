# Conditions and loops
scores = [75, 45, 85, 60, 32]

for score in scores:
    if score >= 75:
        result = "Distinction"
    elif score >= 50:
        result = "Pass"
    else:
        result = "Fail"
    print(score, result)

passed_count = 0
for score in scores:
    if score >= 50:
        passed_count += 1

print("Passed:", passed_count)
