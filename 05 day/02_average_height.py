# student_heights = [180, 124, 165, 173, 189, 169, 146]

student_heights = input("Enter a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

count = 0
total = 0
for height in student_heights:
    total += height
    count += 1

avg_height = round(total / count, 2)

print(f"Average height of this group of students is {avg_height}")