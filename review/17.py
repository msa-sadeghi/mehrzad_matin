class Person:
    def __init__(self, n, f,a):
        self.name = n
        self.family = f
        self.age = a
    def talk(self):
        print(f"{self.name} is talking...")

p1 = Person("mehrbod", "noemani",12)
print(p1.name)
print(p1.family)
p1.talk()
p2 = Person("mehrbod2", "noemani2",16)
print(p2.name)
print(p2.family)
p2.talk()

class Student(Person):
    def __init__(self, n, f, a, stn, g):
        super().__init__(n, f,a)
        self.student_number = stn
        self.grade = g
    def take_exam(self):
        print(f"{self.name} with {self.student_number} is giving an exam...")

s1 = Student("sn", "sf",12,12345 , "A")
s1.talk()
s1.take_exam() 
class Teacher(Person):
    def __init__(self, n, f, exp):
        super().__init__(n, f)
        self.exp = exp
    def test_the_students(self):
        print(f"{self.name}  is testing students...") 

t1 = Teacher("tn", "tf", 15)

t1.talk()
t1.test_the_students()