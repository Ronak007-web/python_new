########################################################################## loops ####################################################################################################
# While loop 
# count = 1                                     
# while count <=5 :                                  # this is infinite loop because it will run forever until we stop it manually # ( count<=5) yeh condition hai jo agar fulfill hota hai toh jo print me likha hota hai woh output ke form me aayega !!
#     print("hello world")
#     count += 1 

# n=int(input("enter the number , whose table you may want :"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# i = 1                                              # maxium time hum iterator (i) ko chote variable me lete hai . 
# while i <=10 :
#     print("right",i)
#     i+=1

# i=5                                                # this called initialization 
# while i>=1:                                        # for this condition that initialization will be true 
#     print(i)                                       # what show on the terminal after run
#     i-=1                                           # for continuing the iterator

# Question 1 :-
# print number from 1 to 100 
# i=1
# while i<=100:
#     print(i)
#     i+=1

# Q 2 :- print the number from 100 to 1 .
# i=100
# while i >=1 :
#     print(i)
#     i-=1

# Q 3 :- print the table of n number for till 10 ..
# n = int(input("Enter the number whom you want table : "))
# i=1
# while i<=10 :
#     print(i*n)
#     i+=1

# Q 3 :- 
# num = [1,4,9,16,25,36,49,64,81,100]
# # print(num[0])                                   # this is manually way to print without using loop 
# # print(num[1])
# # print(num[2])
# # print(num[3])                                   #...... till last num[9]
# # print(len(num))
# index = 0 
# while index < len(num):
#     print(num[index])                             # here num[0] will not print , we've to use index variable to print the value of num[index] 
#     index+=1

#Q 4 :-
# name = [ "Asheesh mishra","mere Ram ji","raunak mishra","teachers","mummy","India"]
# ind=0
# while ind<len(name):
#     print(name[ind])
#     ind+=1
 # jo hum ek ek karke sare elements pe ja rhe hai use " Traverse " kehte hai matlab travel karna elements pe 

#Q5 :-
# num = (1,4,9,16,25,36,49,64,81,100,36)
# x=64
# i=0
# while i < len(num):
#     if(num[i]==x):
#         print("found at i :",i)
#     else:
#         ("founding ...")
#     i+=1

# BREAKS & CONTINUE :-
# Break = hum jaha pe bhi break keyword ko likh denge , hamara loop waha pe hi terimate (ruk) jayega .

# i=1
# while i <=5:
#     print(i)
#     if(i==4):                                      # break ko lagane ke liye pehle if use karenge fir uske baad break lagate hi ruk jayega 
#         break
#     i+=1

# Continue = yeh current iteration ( jo abhi turn chal rhi hai ) Use terminate karta hai , aur fir next iteration ki taraf badh jata hai . 
# opposite to break keyword

# i=0
# while i<=5:
#     if(i==3):
#         i+=1 
#         continue                                   # isko lagate baad woh iterator neglact hua fir usske baad print hoga 
#     print(i)
#     i+=1

# i=0
# while i <=30:
#     if(i==5):
#         i+=1
#         continue                                   # isko niche wali sari line skip ho jati hai isi liye hum pehle hi iske upper i+=1 lekh dete aage ke iteration check karna ke liye . 
#     print(i)
#     if(i==20):
#         break
#     i+=1

# i=0
# while i <=10:
#     if(i%2 ==0):                                   # agar muje sirf even no. ko negalct kaarna ho . & if(i%2!=0) for odd no. neglaction 
#         i+=1
#         continue
#     print(i)
#     i+=1

# FOR loops                                          # yeh use hota hai for sequence travel in list , tuple , string , dictionary , set etc.

# list = [1,2,3,"ronak",4]
# for el in list :                                   # isme el jo hai woh yaha pe ek variable , value , item hai jisme list ki sari values store hone wali hai aur fir woh print ho karenge 
#     print(el)
 
# string = "helloworld"
# for el in string:
#     print(el)
# else:                                              # yeha pe else optional hota hai iska kaam kuch nahi hota hai , bss aise hi loop ke end me likh dete hai taki humko pata chale ki loop khatam ho gaya hai
#     print("end")

# per else tab execute nahi hoga jab loop ke andar break keyword use kiya gaya ho , agar break nahi hai toh else execute hoga

# string = "helloworld"
# for el in string:
#     if(el=="o"):
#         print("o found")
#         break
#     print(el)
# else:
#     print("end")

# num=[1,4,9,16,25,36,49,64,81,100]
# for value in num:
#     print(value)

# list = [1,4,9,16,25,36,49,64,81,100,25]
# x=25                                                        # we x=25 but we want to know at what index it comes 
# index=0
# for el in list :
#     if(el == x):
#         print("x found at index:",index)
#     index+=1

# range :-
# range is a function which returns a sequence of number , while it starts with  0 by default , and increments by 1 ( by default ),and stop before a specified number.
# print(range(5))

# seq = range(5)                             # isme range(5) yeh denote kar rha hai ki yeh 0 se 4 tak sare numbers store karke chal rha hai  while +1 steps . And isme jo ending number hota hai (5) woh include nahi hota hai range me 
# for i in seq:
#     print(i)
# #OR 
# for i in range(5):                         # isme humne range ko humne stop condition diya hai rnage(stop)
#     print(i)

# for i in range(2,5):                       # isme humne range ko dono start or end condition diya hai , range(start,stop) . And isme starting number count hota hai range me but ending numeber nahi 
#     print(i) 

# for i in range(2,5,2):                      # isme range(start,stop,step) hai strp matlab +2 se increase yaha ho rha hai 
#     print(i)

# for i in range(0,12,2):
#     print(i)

# Q 1 :- print number from 1 to 100.
# for el in range(1,101):
#     print(el)

# Q 2 :- print numbers from 100 to 1.
# for i in range(100,0,-1):                     # step by -1 to go 100 to 1
#     print(i)

# Q 3 :- print multiplication table of a number n.
# n= int(input("enter any number:"))
# for i in range(1,11):
#     print(i*n)

# PASS statement :-
# pass is a null statement that does nothing. it is used as faltu ya jabardasti for future code .

# for i in range(5):
#     pass                                     # for future ke liye agar kuch edit karn ho toh 
# print("done")

# if i>5:
#     pass

# Q 1 :- WAP to find the sum of first n number.(using For).
# n = 5                        # kitne numbers tak jaana hai
# sum = 0                      # total ki starting value
# for i in range(1, n+1):      # i = 1,2,3,4,5
#     sum += i                 # total mein i add karo
# print("total sum=", sum)     # final total print karo

# using While loop

# n=5
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)

# Q 2 :- WAP to find the factorial of first n number.(using for).
# n=5
# sum=1
# i=1
# while i<=n:
#     sum*=i
#     i+=1
    # print(sum)













n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
    print(fact)

# n= 5
# factorial = 1
# for i in range(1,n+1):
#     factorial*=i
#     print(factorial)






