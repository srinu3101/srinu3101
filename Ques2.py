#write a program to accept marks of 6 students and display them in a sorted manner
marks=[]
for i in range(6):
    students_marks=int(input(f"enter the students marks{i+1}:"))
    marks. append(students_marks)
    marks.sort()
print("the sorted list of marks is ",marks)
    

