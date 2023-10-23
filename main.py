class Person:

   def __init__(self, name, age, gender):

       self.name = name

       self.age = age

       self.gender = gender

class Teacher(Person):

   def __init__(self, name, age, gender, subject):

       super().__init__(name, age, gender)

       self.subject = subject

   def teach(self):

       print(f"{self.name} is teaching {self.subject}")

class Student(Person):

   def __init__(self, name, age, gender, courses):

       super().__init__(name, age, gender)

       self.courses = courses

   def enroll(self, course):

       self.courses.append(course)

class Subject:

   def __init__(self, name, description, teachers):

       self.name = name

       self.description = description

       self.teachers = teachers

class Course:

   def __init__(self, name, description, students, teachers):

       self.name = name

       self.description = description

       self.students = students

       self.teachers = teachers

class Academy:

   def __init__(self, name, courses, teachers, students):

       self.name = name

       self.courses = courses

       self.teachers = teachers

       self.students = students


