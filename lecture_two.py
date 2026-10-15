# Concatenating Strings 
# str_1 = "Hello"
# str_2 = "World"
# print(str_1 +  str_2) 

# str3 = "  hello i am rounak. \n     a innovator in technology field.  "
# print(str3)

# str4 = " hello eveyone \t i am a student."      # \t is used for tab space and \n is used for new line   
# second="collage"
# print((str4 + second))

# str5 = 'inovaotr' 
# str6 = "enterpreneur"
# print(len(str5 + str6))                         # everything has count of characters in it.for len()
# str= "hello view"
# print(str[5])
# print(str[0:5])
#print(str[0:8],str[0:8:9])
# print(str[5:10]) 
# # or hum len(str) ka bhi use kar skte hai
# print(str[5:len(str)])                          # yeha pe humne str ke length ka use kiya hai taki humko last tak ka character mil jaye
# # or agar last me kuch bhi nahi likhte hai toh python automatically end tak le leta hai
# print(str[5:])
# str = "helloview"
# print(str[-5:-1])
# # # print(str[-7:0])                              # yeha pe humne -7 se 0 tak ka character print karne ke liye bola hai but yeha pe 0 ka koi character nahi hai isliye kuch bhi print nahi hoga
# # print(str[-7:-1])

# str2= " my name is Raunak Mishra "
# print(str2.endswith("hra "))      # yeha pe sirf last ke exact ending character dalne pe liye true milta hai otherwise false milta ha
# print(str2.endswith("jat"))
# print(str2.startswith(" my"))     # yeha pe sirf starting ke exact starting character dalne pe liye true milta hai otherwise false milta hai

# str = "i am coder "
# str3 = str.capitalize()
# print(str3)  OR 
# print(str.capitalize())
# print(str.replace("coder","founder"))
# # OR    
# str4 = str.replace("coder","founder")
# print(str4)
# print(str.replace("o","a"))

# str = "i am coder and hyper"
# print(str.find("e"))
# print(str.find(" "))   
# print(str.find("x"))       # agar koi character nahi hai toh ye -1 return karega

# str = "i am coder and hyper and hero"
# print(str.count("and"))
# print(str.count(" "))
# print(str.count("a"))

# question 1 
# variable = input(" Enter first name : ")
# print("thanks",variable )
# print("Length of the name is :",len(variable))
# print("Length of the nameis :",len(variable.strip()))  # yeha pe humne strip ka use kiya hai taki jo bhi extra space hai wo remove ho jaye

# question 2
# str = " i am hero ith money of $ of 1000000 "
# print(str.count("$"))

#my_age = 19                                       # yeh hmamara input hai 
#if(my_age >= 18):                                 # yeh conditions hai 
    # print("you are eligible ")                   # tab yeh print hoga        
    # print("you are eligible for driving license")    

# question 3
# light = "white"
# if(light == "red"):
#      print("stop")
# elif(light == "green"):
#      print("go")
# elif(light == "yellow"):
#      print("wait")
# else:
#      print("light is broken")

# print("hope you have got it ")

# num = 5 
# if(num > 2):
#     print("number is greater than 2")
# if(num >3):
#     print("number is greater than 3")

# age = 12
# if(age >= 18):
#     print("can vote")    # yeh jo spaces hai ise indentation kehte hai. yehi python ka syntax hai
# else:
#     print("cannot vote")

# marks = int(input("Enter your marks: "))
# if(marks >=90 and marks<=100):
#     print("Grade :" , " A " , " with marks of ", marks)
# elif(marks>=80 and marks<=90):
#     print("Grade :" , " B " , " with marks of ", marks)
# elif(marks>=70 and marks<=80):
#     print("Grade :" , " C " , " with marks of ", marks)
# elif(marks>=60 and marks<=70):
#     print("Grade :" , " D " , " with marks of ", marks)
# elif(marks>=50 and marks<=60):
#     print(" Grade E :","with marks of ",marks)
# elif(marks>=40 and marks<=50):
#     print("Grade :", " f ", " with marks of :", marks)

# else:
#     print("student has failed")
#     print("better luck next time ")
    
# age = 45
# if(age>=18):             # yeh true hoga toh hi niche ke if chalega otherwise else chalega
#     if(age>75):          # jab chal jayega toh iska if and else chalega otherwise main if ka else chalega              
#         print("you cannot drive")
#     else:
#         print("you can drive")
# else:
#     print("cannot be driven")

# # Question 2 
# number = int(input("Enter a number :"))
# if(number%2 == 0):
#     print("number is even")
# else:
#     print(" number is odd")

# Question 3
# a = int(input(" enter a :"))
# b = int(input(" enter b :"))
# c = int(input(" enter c :"))
# if(a>b and  a>c):
#     print(" a is greater ")
# elif(b>c and b>a):
#     print("b is greater ")
# elif(c>a and c>b):
#     print("c is greater ")
# elif(a>b and a==c):
#     print("a and c are eqaul and greater than b")
# elif(b>a and b==c):
#     print("b and c are eqaul and greater than a")
# else:
#     print("all are equal")

# number = int(input("Enter a number :"))
# if(number%7 == 0):

#     print("number is divisible by 7 ")
# else:
#     print("number is not divisible by 7 ")

# self try question 

# print(" this is a traffic light","and age verification program ")
# age = int(input("Enter your age :"))
# light = input ("Enter the color of traffic light :")
# if(age >=18):
#     if(age>75):
#         print("you don't have to drive ")
#     else:
#         print("you can drive ")
# else:
#     print("you cannot drive ")

# if(light == "green"):
#      print(" but if you want or have any urgency so you can go")
# elif(light == "red"):
#      print("you have to stop")
# elif(light == "yellow"):
#     print("you have to wait")
# else:
#     print("light is broken so you can change the route")

# name = input("Enter your name :")
# print("thanks",name)
# email = input("Enter your email for always keep you updated :")
# print("we have sent a confirmation email to :",email)
# OTP = input("Enter the otp :")
# if(OTP == "1234"):
#     print("your email is verified ")
# else:
#     print(" Wrong OTP please try again ")

# print("done with the program ")
name = input("Enter your name : ")
number = int(input("Enter your phone number : "))
Email = input("Enter your email :")
print(" thanks for providing your details we will keep you updated on your",Email,"email")
print(" Now for complete your email verification we have sent a verification OTP to you so please check it and give us only",name )
OTP = input("Enter the OTP : ")
if( OTP == "1234" or OTP == "5678" or OTP == "8511"):
    print("your email is verified ")
else:
    print(" Wrong OTP please try again ")

###################################################################### THANK YOU #################################################################################################