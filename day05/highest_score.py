student_heights = input("Input a list of student score ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    if int(student_heights[0]) < int(student_heights[n]):
        student_heights[0] = student_heights[n]
print("The highest score in the class is : {}".format(student_heights[0]))