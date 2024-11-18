class Person:
    def __init__(self, n, f):
        self.name = n
        self.family = f
    def talk(self):
        print(f"{self.name} is talking...")

p1 = Person("mehrbod", "noemani")
print(p1.name)
print(p1.family)
p1.talk()
p2 = Person("mehrbod2", "noemani2")
print(p2.name)
print(p2.family)
p2.talk()





# class Student(Person):
#     def __init__(self, n, f, stn):
#         super().__init__(n, f)
#         self.student_number = stn
#     def take_exam(self):
#         print(f"{self.name} with {self.student_number} is giving an exam...")
    
# class Teacher(Person):
#     def __init__(self, n, f, exp):
#         super().__init__(n, f)
#         self.exp = exp
#     def test_the_students(self):
#         print(f"{self.name}  is testing students...") 
# s1 = Student("sn", "sf", 12345)
# t1 = Teacher("tn", "tf", 15)
# s1.talk()
# t1.talk()
# t1.test_the_students()