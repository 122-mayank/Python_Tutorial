
# Instance Attrbiutes
class Student:

    def study(self):
        print("Student is studying!!")

    def __init__(self , name , age):
        self.name = name
        self.age = age

s1 = Student( "Mayank" , 23)
s2 = Student( "Rahul", 21)

print(s1.name , s2.name , end =" ")
print(s1.age , s2.age, end=" ")
print(s1.study())

# self refers to current object 
# __int()__ is a constructor in python


        