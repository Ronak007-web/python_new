######################################################## OBJECT ORIENTED PROGRAMMING PART 1 ########################################################

# For creating a class we use the keyword "class" followed by the name of the class. The name of the class should start with a capital letter.
class Student:
    name = "rounak"                            # this is the features for each and every object of the class. 
    age=18

# for creating an object of the class we use the name of the class followed by parentheses.
# s1 = Student()                       # here , s1 is an object of the class Student.
# print(s1.name)                       
# print(s1.age)

# s2=Student()
# print(s2.name)
# print(s2.age)

# this will give same output kyuki humne class me fixed features define kiye hai jo sare objects ke liye same hoga. but agar hum chahte hai ki har object ke liye alag features ho toh hum constructor ka use karenge.

# class Car:
#     colour="black"
#     size="1000cc"

# car1 = Car()
# print(car1.colour)
# print(car1.size)

# __init__() function :- it is a constructor function which is used to initialize the features of the class. it is automatically execute when we create an object of the class.
# class Student:

#     def __init__(self,name,age,marks):                 #  self hamesa first object ko denote karta hai aur uske value asign karne ke liye use hota hai. fir dusre object ke liye fir se self ka use hoga aur uske value asign karne ke liye use hoga. isliye humne self ka use kiya hai.    # and iske baad ke jo bhi parameters hai ewoh feasture ko denote karte hai matlab pehle self fir uske baad ke parameters feature denote karenge jese :- fullname,age,address,city etc 
#         self.name = name
#         self.age = age
#         self.marks = marks
#         # print(self)             # self=s1           # idhar self ka matlaba hai jo new object create ho rhi hai.                       
#         print("adding new student in database")
              
# s1 = Student("rounak",18,90)                               # ime hame init function me jo jo features define kiye gye hai uske hisab se hame idhar bhi Student() me value dalna hoga jese :- name,age,marks. otherwise error aayega. and iske baad jo bhi value humne Student() me di hai woh init function me self ke sath assign ho jayegi.
# print(s1.name)  

# s2 = Student("jatayu",20,85)
# print(s2.marks)

# class Student:
#     collage="apnacollage"
# #     def __init__(self,name,age,marks):
#         self.name=name
#         self.marks=marks
#         self.age=age
#         print("entering all stuffs of students")

# s1=Student("rounak",14,89)
# print(s1.name,s1.age,s1.marks)
# print(s1.name)                          

# s2=Student("jatayu",15,90)
# print(s2.name,s2.age,s2.marks)
# print(s2.collage)         
# #OR
# print(Student.collage)                         # agar hum class.feature bhi print karvenge toh bhi same output aayega.(print(s1.collage)) ki tarah.

# class Student:
#     collage="apnacollage"
#     name="nothing"
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.marks=marks
#         self.age=age
#         print("entering all stuffs of students")

# s1=Student("rounak",14,89)
# print(s1.name)                   #here obj.atr > class.atr thats why rounak print hua na ki nothing.
# # print(s1.collage)

# class Student:
#     def __init__(self,name,mark):         # defining the contructor function 
#         self.name=name
#         self.mark=mark

#     def welocme(self):                    # defining the method(function) of the class
#         print("welcome student:",self.name)

#     def your_name(self):   
#         print("Your marks is :",self.mark)

# s1=Student("rounak",99)                  # entering the values of the features of the class through constructor function
# print(s1.name,s1.mark)

# s1.welocme()
# s1.your_name()

#Q 2 :- Create student class that takes name & marks of 3 subject as argumnets in constructor. then create a method to print the average.
# class Student:
#     def __init__(self,name,sub1,sub2,sub3):
#         self.name=name
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3

#     def average(self):
#         print("average of 3 subjects is :", self.sub1+self.sub2+self.sub3/3)
#     @staticmethod                 # decorator :- ek function hai jo paramter me bhi function leta hai aur ouput me bhi function let hai. isse hum function ke behaviour ko change kar sakte hai. 
#     def hello():
#         print("hello")

# s1=Student("rounak",90,80,70)
# # print(s1.name,s1.sub1,s1.sub2,s1.sub3)
# s1.average()


# Abstraction  iska matalab ki user ko unnessary , and huge details na dikha ke sirf requird essential things dikhana .

# class car:
#     def __init__(self):
#         self.acc=False
#         self.brk= False
#         self.clutch=False

#     def start(self):
#         self.clutch=True         # this is unnecessary details for the user. user ko sirf yeh chahiye ki car start ho rhi hai ya nahi. baki details unko nahi chahiye. so we can hide these details from the user by using abstraction.
#         self.acc=True            #same 
#         print("car started")

# car1=car()
# car1.start()

# Encapsulation :- iska matalab ki class me data and function ka use karke object banana . jo abhi tak wohi kar rhe the

# Q3:- Create Account class with 2 attributes - balance & account no. , Create method for debit,credit&printing he balance.

# class Account:
#     def __init__(self,balance,accountnumber):
#         self.balance=balance
#         self.accountnumber=accountnumber

#     def debit(self,amount):
#         self.balance-=amount
#         print("rs,",amount,"was debited")
#         print("total balance :",self.balance)


#     def credit(self,amount):
#         self.balance+=amount
#         print("rs",amount,"was credited")
#         print("total balance :",self.balance)
        

#     def printblance(self):
#         print("balance is sufficient :", self.balance)


# account1=Account(1000,123456789)
# print(account1.balance)

# account1.debit(100)
# account1.credit(500)
# account1.printblance()








