class Student:
  def __init__(self,name,age,grade):
    self.name = name
    self.age = age
    self.grade = grade

  def get_grade(self):
    return self.grade

class Course:

  def __init__(self,name,max_students):
    self.name = name
    self.max_students = max_students
    self.students = []

  def add_student(self,student):
    if len(self.students) < self.max_students:
      self.students.append(student)
    else:
      print("TOO MANY GODDAMN PEOPLE")
    
  def get_avg_grade(self):
    grades = [student.get_grade() for student in self.students]
  
    return round(sum(grades)/len(grades),2)



math = Course("math",25)

s = Student("bob",18,70)

s2 = Student("rob",19,67)

s3 = Student("Stiven",24,98.78)




math.add_student(s)
math.add_student(s2)
math.add_student(s3)


print(math.get_avg_grade())

