class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Course:
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

class Student(Person, Course):
    def __init__(self, name, age, course_name, duration):
        Person.__init__(self, name, age)
        Course.__init__(self, course_name, duration)
    
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)

student = Student("Alice", 22, "Computer Science", "4 years")
student.display_info()
