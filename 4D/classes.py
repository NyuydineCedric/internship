class Student:
    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
student1 = Student("Cedric", 4.0)
student2 = Student("Joe", 3.8)
student3 = Student("Jim", 3.2)
print(Student.get_count())