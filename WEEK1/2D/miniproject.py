total_students = 0
passed_students = 0

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "Fail"

student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_course = input("Enter course: ")
student_marks = int(input("Enter marks: "))

grade = calculate_grade(student_marks)

student_record = {
    "name": student_name,
    "age": student_age,
    "course": student_course,
    "marks": student_marks,
    "grade": grade
}

print("\nHere is your Result")
print(f"Name: {student_record['name']}")
print(f"Age: {student_record['age']}")
print(f"Course: {student_record['course']}")
print(f"Marks: {student_record['marks']}")
print(f"Grade: {student_record['grade']}")