########################################################### FUNCTIONS ############################################################################


# def calc_sum(a,b):             # isme def ka matlab hai defining the function aur calc_sum function ka naam hai aur (a,b) ye parameters hai jo input hota hai
#     sum=a+b                    # diye gaye input ka me kya karna chahta hu isko define kar raha hu ( ex:- by doing sum)
#     print(sum)                 # ab usi kaam ko me print karna chahta hu
#     return sum                 # iska matlab ki hum output ko return karna chahta hu taki hum usko kisi variable me store kar sake 

# calc_sum(10,20)

# niche wale ke bajaye hum simple upper wala likh sakte hai jisse code jaldi ho jaye aur simple ho jaye
# a=10
# b=20
# sum=a+b
# pprint(sum)

# a = 12
# b = 23
# sum = a + b
# print(sum)

# and jo calc_sum() ke values hai jo humne shortcut se find kiya tha.
# woh sab calc_sum(parameter) ke jakar store ho jayega.

#Function definition
# def calc_sum(a,b,s):       # parameters are (a,b,s)
#    return a+b+s

# sum=(calc_sum(3,4,5))      # function call where (3,4,5) are arguments jo parameters me store ho jayenge aur fir function ke andar kaam karenge
# print(sum)

# def print_hello():           # iska matalab jab bhi me print_hello() likhunga toh hello world print hoga
#     print("hello world")

# print_hello()
# print_hello()

# output=print_hello()
# print(output)                 # yeh none print karega kyuki humne function ke andar return nahi kiya hai isliye output me kuch bhi nahi aayega

#Q 1 := find out the average of three number 

# def calc_avg(a,b,c):
#     avg=(a+b+c)/3
#     print(avg)
#     return avg

# average_of(10,20,30)    

# built in function      
# 1.print()
# print("apna")                 # seperator = " "  # by default seperator = " " hota hai jo ki space me print kar deta hai
# print("collage")              # end = "\n"  # by default end = "\n" hota hai jo ki new line me print kar deta hai

# but we want to print both string in same line then we can use end = " " 
# print("apna",end=" ")                # isme end = " " ka matlab hai ki dono string ko same line me print karna hai
# print("collage")

# 2.len()
# 3.type()
# 4.input()
# 5.range()

# User defined function = jo hum khud define karte hai aur uska kaam bhi hum khud define karte hai

# DEFAULT PARAMETERS = aise values jo tab use hongi jab koi argument pass nahi hoga


# def calc_mult(a=1,b=2):           # this ( a=1 , b=1 ) is the default matlab agar hum koi bhi argument pass nahi karenge tabhi yehi a=1 and b=1 man liya jayega
#     print(a*b)
#     return a*b                   # yeh as a output milega

# calc_mult(3,4)
# calc_mult()

# here we can do (a,b=1) but not (a=1,b) .

# Q1 :- WAF TO PRINT THE LENGTH OF A LIST.(LIST IS THE PARAMETER)

# cities = ["surat","mumbai","kazakhstan"]
# name = ["rounak","mishra"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(name)

# Q2:- WAF to print the elements of a list in a single line.(list is the [parameter])

#  = ["surat","mumbai","kazakhstan"]

# print(cities[0],end=" ")              # end=" " ka matlab jo iske pehle likha tha woh aur jo niche print mw likha hai woh dono same line me print ho jayegenge 
# print(cities[1],end=" ")
# OR 
# def print_list(list):               # yeh hamara function hai jisme humne list ko parameter ke roop me liya hai aur fir uske elements ko print karenge
#     for el in list:                 # yeha pe el ek variable hai jisme list ke elements store honge aur fir woh print ho karenge
#         print(el,end=" ")           # jab bhi hum dubara kabhi is function ko use karenge toh woh isi format me print hoga 

# print_list(cities)

# Q3 :- WAF to find the factorial of n number. ( n is the parameter)
# according to for loop 
# n=10
# fact=1
# for i in range(1,n+1):
#     fact*=i
#     print(fact)

n=5
fact=1
for i in range(1,n+1):
    fact*=i
    print(fact)
    i+=1
    
#according to function loop
# def calc_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#         print(fact)

# now function setup ho gya hai now jis bhi n number ka factorial find karna hai usko hum function ke andar pass karenge aur woh uska factorial print karega
# calc_fact(10)

# calc_fact(11)

# Q4 :- WAF to convert USD TO INR ( n is the parameter)

# def usd_to_inr(n):
#     INR = n*82.74
#     print(n,"USD =", INR,"INR")
#     return INR

# usd_to_inr(4)

# Q5 :- WAF where n number identify as even and odd.

# def identify_num(n):
#     if(n%2==0):
#          print("Even")
#     else:
#          print("odd")

# identify_num(10)

# identify_num(9)

# RECURSION FUNCTION
# it means that function call itself again and again until it reach to the base case.

# question is that we have to print the number from n to 1 using recursion function.
# def show(n):                    # funuction defined
#     if(n==0):                   # last me humne base case define kiya hai ki jab n=0 ho jaye toh function ko stop kar do
#         return                  # yeh return statement function ko stop kar deta hai
#     print(n)                    # yeh hume dikhta hai ki function kaam kar raha hai aur n ko print kar raha hai
#     show(n-1)                   # yeh function call hai jisme humne n-1 pass kiya hai jisse function fir se call hoga aur fir se print karega aur fir se call hoga jab tak n=0 nahi ho jata

# show(2)

# fact(n) = fact(n-1)*n
# fact(n-1) = fact(n-2)*(n-1)

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1)*n

# print(fact(4))


# Q1:- Write a recrusive function to calculate the sum of n natural numbers.

# def natural_num(n):
#     if(n==-1):
#         return 0 
#     return natural_num(n-1)+n

# print(natural_num(4))

# Q2:- Writew a recursive function to print all elements in a list.

# list = ["erounak","mishra",2,4,5]

# def el(list,index):
#     if(index==len(list)):
#         return 
#     print(list[index])
#     return el(list,index+1)

# el(list,0)










