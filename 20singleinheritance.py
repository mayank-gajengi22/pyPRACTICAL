class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, grade):
   
        super().__init__(name, age)
        self.roll_no = roll_no
        self.grade = grade
    
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Grade:", self.grade)


student = Student("John Doe", 20, "A123", "A")
student.display_info()
