n = int(input("Enter the number of students: "))
student_marks = {}
for i in range(n):
    name, *marks = input(f"Enter the marks for student {i+1}: ").split()
    marks = list(map(float, marks))
    student_marks[name] = marks

query_name = input("Enter the name of the student to find the average marks: ")
if query_name in student_marks:
    avg_marks = sum(student_marks[query_name])/len(student_marks[query_name])
    print("{:.2f}".format(avg_marks))
else:
    print("Student not found.")