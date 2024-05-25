# import random

# print(random.random())
# print(random.randint(0,10))

# l=["hi","hello","Bye",45,457,False]
# print(random.choice(l))


# inheritance => single,muliple,multilevel,hierarchical

# base class(parent)
# derived class(child)

# class Myclass:
#     def __init__(self):
#         self.__a=34

#     def disp(self):
#         print(self.__a)
        
# obj=Myclass()
# obj.disp()
# print(obj.__a)


# # Multiple
# class A:
#     def __init__(self):
#         self.a=24

#     def display(self):
#         print("A :",self.a)

# class B:
#     def __init__(self):
#         self.b=51

#     def display1(self):
#         print("B : ",self.b)

# class C(A,B):
#     def __init__(self):
#         self.c=67
#         A.__init__(self)
#         B.__init__(self)

#     def display2(self):
#         print("C : ",self.c)

# obj=C()

# obj.display()
# obj.display1()
# obj.display2()


# Multilevel
# class A:
#     def __init__(self):
#         self.a=24

#     def display(self):
#         print("A :",self.a)

# class B(A):
#     def __init__(self):
#         self.b=51
#         A.__init__(self)

#     def display1(self):
#         print("B : ",self.b)

# class C(B):
#     def __init__(self):
#         self.c=67
#         B.__init__(self)

#     def display2(self):
#         print("C : ",self.c)

# obj=C()

# obj.display()
# obj.display1()
# obj.display2()


# Hierarchical
# class A:
#     def __init__(self):
#         self.a=24

#     def display(self):
#         print("A :",self.a)

# class B(A):
#     def __init__(self):
#         self.b=51
#         A.__init__(self)


#     def display1(self):
#         print("B : ",self.b)

# class C(A):
#     def __init__(self):
#         self.c=67
#         A.__init__(self)

#     def display2(self):
#         print("C : ",self.c)

# bobj=B()
# cobj=C()

# bobj.display()
# bobj.display1()

# cobj.display()
# cobj.display2()


# Bobj=B()

# Bobj.display()
# Bobj.display1()

# class C:
#     def __init__(self):
#         self.c=100
        
#     def madhav(self):
#         print("C :",self.c)

# obj = C()
# obj.madhav()


# Person  -> name ,age
# department -> deptname,salary

# class Person:
#     def __init__(self):
#         self.name='madhav'
#         self.age=21
        
#     def display(self):
#         print("Name is: ",self.name)
#         print("Age is: ",self.age)
        
# class Department(Person):
#     def __init__(self):
#         self.depart='barcelona'
#         self.salary=50000
#         Person. __init__(self)
        
#     def display1(self):
#         print("Department is: ",self.depart)
#         print("salary is: ",self.salary)
        
# department = Department()
# department.display()
# department.display1()
        

# obj = Person()
# obj.display()



# stone,paper,scissor
# computer 
# user 

# c=2
# u=1

# paper
# stone
# user win

# paper
# paper
# draw

# stone
# scissor
# computer win


# user -> 1 point
# computer -> 3 pointer


# OM , krish,Karm




# 5 question
# 1. what is html?
# a
# b
# c
# d

# b

# 2. what is html?
# a
# b
# c
# d

# d



# right
# wrong
# point

# point -> 5



# student -> name,age,rollno
# marks -> hindi,science,math
# percentage ->percentage

class Student:
    def __init__(self):
        self.name='madhav'
        self.age=21
        self.rollno=1
        
    def display(self):
        print("Name is: ",self.name)
        print("Age is: ",self.age)
        print("Rollno is: ",self.rollno)
        
class Mark(Student):
    def __init__(self):
        self.hindi=95
        self.science=80
        self.math=70
        Student.__init__(self)

    def display1(self):
        print("Hindi mark: ",self.hindi)
        print("Science mark: ",self.science)
        print("Math mark: ",self.math)
        
class Percentage(Mark):
    def __init__(self):
        Mark.__init__(self)
        self.percentage=((self.hindi+self.science+self.math)/3)
        
    def display2(self):
        print("Your percentage: ",self.percentage)
        
obj=Percentage()

obj.display()
obj.display1()
obj.display2()