class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls , new_school):
        cls.school =new_school

Student.change_school("XYZ School")

s1 = Student()
print(s1.school)

print(Student.school)

"""
cls refers to the class.

Conceptually:

self → current object
cls  → current class
"""