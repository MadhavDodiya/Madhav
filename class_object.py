# class = variables,functions
# object

# class first:
#     a=34
#     b="Hii"

#     def display(self,x,y):
#         print(self.a,self.b,x,y)

# obj=first()
# obj1=first()

# obj.display(2,3)



# create a classs circle and display area of circle

# create a class person display name,age,salary of a person
# import math
# class circle:
#     area = math.pi
#     radius=int(input("Enter radius : "))

#     def display(self):
#         print("Area is  : ")
#         print((self.area*self.radius*self.radius))

# obj=circle()
# obj.display()



# constructor =>default,parameterized

class first:

    def __init__(self,x,y):
        self.a=x
        self.b=y
        

    def display(self):
        print(self.a,self.b)

obj=first(23,"BR")
obj2=first(56,"sr")
obj.display()
obj2.display()