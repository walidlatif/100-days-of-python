student_heights = input("Input a list of student heights ").split()
sum = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum += student_heights[n]
div = sum / len(student_heights)
print(f"{round(div)}")
