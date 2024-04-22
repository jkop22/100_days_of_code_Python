student_scores = {
    "Jan": 81,
    "Franta": 78,
    "Karel": 99,
    "Tereza": 74,
    "Jane": 62
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Beyond Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
    
print(student_grades)