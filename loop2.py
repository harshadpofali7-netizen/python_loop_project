#Mini project 2 : Student marks and grade report
num_students = int(input("Enter the number of students in the class:"))
total_marks = 0.0
pass_count = 0
fail_count = 0
student_report = []
for i in range(1, num_students + 1):
    print(f"\n---Student{i}---")
    name = input("Enter student name: ")
    while True:
        marks = float(input("Enter marks (0 to 100): "))
        if 0 <= marks <= 100:
            break
        print("Invalid entry! marks must be between 0 to 100.")
    total_marks += marks
    if marks >= 75:
        grade = "A"
        pass_count += 1
    if marks >= 60:
        grade = "B"
        pass_count += 1
    if marks >= 50:
        grade = "C"
        pass_count += 1    
    if marks >= 40:
        grade = "D"
        pass_count += 1
    else:
        grade = "Fail"
        fail_count += 1
    student_report.append(f"{name}: Grade {grade} ({marks} marks)")
if num_students > 0:
    class_average = total_marks/ num_students
else:
    class_average = 0.0
print("\n============================")
print("   CLASS PERFORMANCE REPORT   ")
print("==============================")
print("\n---student garde---")
for report in student_report:
    print(report)
print("\n---Summary Statistics---")
print(f"Class average: {class_average}")
print(f"Pass count: {pass_count}")
print(f"Fail count: {fail_count}")
print("===================================")
