class Student:
    school ="ABC School"  # this is class attribute


    def __init__(self , name):
        self.name = name

s1 = Student("Mayank")
s2 = Student("Rahul")


print(s1.school)
print(s2.school)