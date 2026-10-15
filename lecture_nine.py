############################################################################ OOPs Part 2 ##########################################################################################
# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student("rounak")

# del s1.name                 # deleting the feature of the class using del keyword. if we try to print the feature after deleting it then it will give an error.
# print(s1)

# del s1                      # deleting the object of the class using del keyword. if we try to print the object after deleting it then it will give an error.
# print(s1)

# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass                  # by doing this __acc_pass become private feature which can't be acccessed by anyone outside the class 

#     def reset_pass(self):
#         print("your password is :",self.__acc_pass)

# acc1=account(12345,"abcd")
# # print(acc1.acc_pass)
# print(acc1.reset_pass())      # this will show the password because method can access the private feature of the class but if we try to access the private feature of the class outside the class then it will give an error.

# class person:
#     __name="nothing" 

#     def __hello():              # this is how we can private the method too , by putting __ before the method name.
#         print("hello world")
# p1= person()
# # print(p1.__name)          # this will give an error because __name is a private feature of the class and it can't be accessed outside the class.
# print(p1.hello())

# class person:
#     name= "nothing"
#     def __hello(self):          
#         print("hello person")

#     def welcome(self):
#         self.__hello()                 # this how we can use that private method by this welcome method which is public and can be accessed outside the class.

# p1=person()
# print(p1.welcome())


# In short we can access the private feature and method or anything only in the class by internally but not outside the class.
# but if we want to access the private things outside the class then we have to go via any new method on that class which is public and then by this we can access the private things of the class.

# Inheritance:- iska matlab ki hum ek class ke features ya method ko dusre class me use kar sakte hai. 
# single Inheritance:- isme hum ek hi claas ko dusre claas me use kar sakte hai uske metod or fweaturs

# class Car:
#     colour="black"
#     @staticmethod
#     def start():
#         print("car has started")

#     @staticmethod
#     def stop():
#         print("Stoped")

# class BMWcar(Car):              # by this hum us car ke features na dmethod ko is BMWcar class me use kar sakte hai. 
#     def __init__(self,name):
#         self.name=name

# car1=BMWcar("rounak express")
# print(car1.start())
# print(car1.colour)

# Mutli Inheritance:- isme hum ek se jyada class ke features or method ko dusre class me use kar sakte hai.

# class Car:
#     colour="black"
#     @staticmethod
#     def start():
#         print("car has started")

#     @staticmethod
#     def stop():
#         print("Stoped")


# class Toyoto(Car):              
#     def __init__(self,brand):
#         self.brand=brand
        

# class fortuner(Toyoto):
#     def __init__(self,model,gas_type):
#         self.model = model
#         self.gas_type = gas_type

# car1=fortuner("rounak fortuner","petrol")
# print(car1.start())
# print(car1.gas_type)
# car1=Toyoto("rounak toyoto")


# class A:
#     varA= "welcome to class A"

# class B:
#     varB= "welcome to class B"

# class C(A,B):                             # by this hum class A and class B ke features or method ko class C me use kar sakte hai.
#     varC= "welcome to class C"

# c1=C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# class car:
#     def __init__(self,type):
#         self.type=type

# class toyot(car):
#    def __init__(self,brand,type):
#        super(). __init__(type)            # isme hum parent class ka constructor ko call kar rahe hai jisse ki hum parent class ke features ko child class me use kar sake.
#        self.brand=brand

# car1=toyot("rounak toyoto","petrol")
# print(car1.type)

# class Person:
#     name="nothing"
    
#     @classmethod                   # iske madat se hum class ke features ko change kar sakte hai.by making this method as class method.
#     def changename(cls,name):
#         cls.name=name

# p1=Person()
# p1.changename("rounak")          # by this we can change the name of the class feature name by using the class method changename.
# print(p1.name)           # rounak
#OR
# print(Person.name)       # rounak

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

# std1=Student(99,99,99)
# print(std1.percentage)

# POLYMORPHISM:- iska matlab ki ek hi method ka alag alag class me alag alag implementation ho sakta hai.
 
#implicit overloading :- jo python ne hamare liye alrdeady class operation bana ke rahna hai 

# print(1+2)                # int addition 
# print("APNA"+"COLLAGE")   # string concatenation(addition)
# print([1,2,3]+[1,2,3])    # list merging(addition)
# defining new complex number class and overloading the addition operator for it

# class complex:
#     def __init__(self,real,imaginary):
#         self.real= real
#         self.imaginary= imaginary

#     def shownum(self):
#         print(self.real,"i","+",self.imaginary,"j")

#     def add(num1,num2):
#         print("Addition of two number is :", num1.real+num2.real,"i","+",num1.imaginary+num2.imaginary,"j")
# num1=  complex(2,4)
# num1.shownum()
# num2= complex(9,9)
# num2.shownum()

# (num1.add(num2))

# i want that when user will come ,they only do this print(num1+num2) that's it
 
# class complex:
#     def __init__(self,real,imaginary):
#         self.real= real
#         self.imaginary= imaginary

#     def shownum(self):
#         print(self.real,"i","+",self.imaginary,"j")

#     def __add__(num1,num2):
#         print(num1.real,num2.real,"i","+",num1.imaginar+num2.imaginary,"j")

#     def __sub__(num1,num2):
#         print(num1.real-num2.real,"i","+",num1.imaginary-num2.imaginary,"j")

   
# complex1 = complex(2,4)
# complex1.shownum()

# complex2 = complex(8,9)
# complex2.shownum()

# complex1-complex2           # now its working because we have overloaded the - operator for our complex class by defining the __sub__ method in it.


# Q 1 :- 
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def Area(self):
#         return (3.14)*self.radius**2

#     def Perimeter(self):
#         return 2*(3.14)*self.radius        # here we can use print(2*3.14*self.radius) also but we are using return because we want to return the value of perimeter to the user.

# circle1=Circle(5)
# print(circle1.Area())
# print(circle1.Perimeter())

#Q 2 :-
# class Employee:
#     def __init__(self,role,department,salary):
#         self.role = role
#         self.department = department
#         self.salary = salary


# class engineer(Employee):
#     def __init__(self,name,age,role,department,salary):
#         super().__init__(role,department,salary)
#         self.name=name
#         self.age=age


#     def showdetails(self):
#             print("name :",self.name)
#             print("age :",self.age)
#             print("Role :",self.role)
#             print("Department :",self.department)
#             print("Salary :",self.salary)
        

# engineer1 = engineer("Rounak", 22, "Founder", "AI and business operation", "1000 cr ")
# engineer1.showdetails()

#Q 3:-
# class Order:
#     def __init__(self,item,prize):
#         self.item=item
#         self.prize=prize

#     def __gt__(order1,order2):                   # here gt means greater than operator which is used to compare the two objects of the class order.
#         return order1.prize>order2.prize


# order1=Order("chips",100)
# order2=Order("Chocolate",200)

# print(order2>order1)
   
################################################################################ ENDED ##########################################################################################################




 









    





  






































