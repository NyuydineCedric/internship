def student_averages(students):
    averages = {}

    for student in students:
        total = 0

        for mark in student["marks"]:
            total = total + mark

        average = total / len(student["marks"])

        averages[student["name"]] = average

    return averages


def top_student(averages):
    highest = 0
    top = ""

    for student in averages:
        if averages[student] > highest:
            highest = averages[student]
            top = student

    return top


students = [
    {"name": "Alice", "marks": [85, 90, 78]},
    {"name": "Bob", "marks": [60, 55, 70]},
    {"name": "Cara", "marks": [95, 92, 89]}
]

averages = student_averages(students)

print(averages)
print("Top Student:", top_student(averages))