class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

class CollegeStudent(Student):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age, roll_no)
        self.course = course
    
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)


student = CollegeStudent("Bob", 21, "B567", "Electrical Engineering")
student.display_info()
