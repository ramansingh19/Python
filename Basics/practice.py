class Student:
    def __str__(self):
        return "Raman"

    def __repr__(self):
        return "Aman"

s = Student()

print(str(s))  
print(repr(s))  
print(s)        