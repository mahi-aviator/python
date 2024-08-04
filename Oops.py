# class Car:
#     color="Red"
#     brand="mercedes"
# car1=Car()
# print(car1.color)
# print(car1.brand)

# class Student:

#     def __init__(self,name,marks ):
#      self.name=name
#      self.marks=marks

#     def get_avg(self):
#        sum=0
#        for val in self.marks:
#            sum+=val
#        print("hi",self.name,"your score is " ,sum/3)  



# s1=Student("karan",[90,88,90])
#s1.get_avg()


# class Account:
#     def __init__(self,bal,acc):
#         self.balance=bal 
#         self.account_no=acc

#     def debit(self,amount):
#         self.balance-=amount
#         print("rs",amount,"was debited") 
#         print("total balance=",self.get_balance()) 

#     def credit(self,amount):
#         self.balance+=amount
#         print("rs",amount,"was credited") 
#         print("total balance=",self.get_balance())    
 
#     def get_balance(self):
#         return self.balance
    
# acc1=Account(00000,74567)
# acc1.credit(142000)
# acc1.debit(15000)   

# class Person:
#     __name="anonymous"

#     def __hello(self):
#         print("Hello Mahima. Why are you sad ?. I love you tumhare bhagwan ji ")

#     def welcome(self):
#         self.__hello()    

# p1=Person()      
# print(p1.welcome())


#to calculate percentage 


# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage=str((self.phy+self.chem+self.math/3))+"%"

#     @property
#     def percentage(self):
#           return str((self.phy+self.chem+self.math/3)) + "%"

# stu1=Student(90,89,98)
# print(stu1.percentage)

# stu1.phy=85
# print(stu1.percentage)


#dunder function 
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def showNumber(self):
#         print(self.real,"+" ,self.img,"j")

#     def __add__(self,num2):
#         newReal=self.real+num2.real
#         newImg=self.img+num2.img
#         return Complex(newReal,newImg)
     
#     def __sub__(self,num2):
#         newReal=self.real+num2.real
#         newImg=self.img-num2.img
#         return Complex(newReal,newImg) 
    
# num1=Complex(1,3)  
# num1.showNumber()

# num2=Complex(2,6)
# num2.showNumber()

# num3=num1-num2 
# num3.showNumber()

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return 3.14*self.radius**2

#     def perimeter(self):    
#         return 2*3.14*self.radius
# c1=Circle(21)

# print(c1.area())
# print(c1.perimeter())
       
# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
    
# from turtle import Turtle , Screen

# timmy_the_turtle=Turtle() 
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# for _ in range(4):
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)
# screen=Screen()
# screen.exitobclick()


# import turtle as t
# import random

# screen = t.Screen()
# screen.setup(width=600, height=600)

# tim = t.Turtle()
# tim.speed(200)  

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#       tim.forward(100)
#       tim.right(angle)
#       tim.color(random.choice(colors))

# for shape_side_n in range(3,10000):
#     draw_shape(shape_side_n)

# t.done()


import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.speed("fastest")

def draw_spirograpgh(size_of_gap):
    for _ in range(int(360/size_of_gap)): 
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograpgh(5)

screen = t.Screen()
screen.exitonclick()

























