############################################################## LIST IN PHYTHON ##########################################################################################


# marks=[65,"ronak","jatayu",87,5.5]  # list always in [] brackets and we can store any type of data in list like int, float, string etc.
# print(marks)
# print(marks[3])
# print(type(marks))
# print(len(marks))
# print(marks[0:2])
# print(marks[0:2])

# # For string we can use indexing and slicing but we cannot change the value of string because string is immutable
# str = "hello"
# print(str[0])
# str[0] = "y"                        # its give error because string is immutable that means we cannot change the value of string

# for list we can use indexing and slicing & also we can change the value of list because list is mutable
# marks = ["ronak","jatayu","hello",]
# marks[0] = "ronak patil"
# print(marks[0])
# print(marks[2])
# marks[1] = "jatayu kumar"
# print(type(marks))
# print(marks)
# marks[3] = "hello world"            # this will give error because we cannot add new value in list by indexing we can only change the value of existing index

# List methods
# list = [ 64,45,67,89,90]
# list.append(100)                    # iska kaam sirf last me ek value add karna hota hai
# print(list)
# print(list.append(18))              # aise karne pe none print hoga.

# list.sort()                         # iska kaam list ke elements ko ascending order me sort out karna hota hai
# print(list)
# list.reverse()                      # iska kaam list ke elements ko reverse karna hota ha
# print(list)
# list.sort(reverse=True)             # iska kaam list ke elements ko descending order me sort out karna hota hai
# print(list)
# list.sort(reverse=True)
# print(list)

## Note :- for string sorting jo hogi woh jis words me kam alphabets honge usse se acsending me sort out hoga 
## Note :- for descending order ke liye jisme jada words honge usse sorting kiya jaiyega 

# list.insert(2,100)                # iska kaam list ke elements me se kisi bhi index ke baad ek value add karna hota hai
# print(list)
# list.remove(45)                   # iska kaam list ke elements me se kisi bhi value ko remove karna hota hai
# print(list)
# list.pop(2)                       # iska kaam list ke elements me se kisi bhi index ke value remove karna hota hai
# print(list)
# list.clear()                        # iska kaam list ke elements me se sabhi value remove karna hota hai
# print(list)

#########################################################  TUPLE IN PHYTHON #################################################################################

# tup = (1,2,3,4,5)                 # tuple always in () brackets and we can store any type of data in tuple like int, float, string etc.
# print(type(tup))
# print(tup[0])
# print(tup[3])
# # tup[0] = 5                      # this operation will give error beacuse tuple is immutable that means we cannot change the value of tuple
# Tup = ()                          # this valid in python because we can create empty tuple           
# print(Tup)
# print(type(Tup))
# tuP = (1,)                        # this is right way to create tuple with single value because we have to put comma after the value
# print(type(tuP))
# print(tuP)
# print(tuP[0:2])                   # in tuple we can also do slicing as same as we have done in list and string
# print(tuP[0:3])

# tuple methods

# tup = (3,6,9,3,8) 
# print(tup.index(3))               # isme hum kisi bhi value ko dalte ha to ye uska index return karega 
# print(tup.count(3))               # isme hum kisi bhi value ko dalte ha to ye uska count return karega ki kitni baar ye value tuple me hai

# Question 1
# print("Enter your 3 favourite movies name ")
# movie1 =(input("Enter first movie name :"))
# movie2 =(input("Enter second movie name :"))
# movie3 =(input("Enter third movie name :"))
# list = [movie1,movie2,movie3]
# print(list)

# or second method 

# movie = []
# movie.append(input("enter your first favourite movie name :"))
# movie.append(input("enter your second favourite movie name :"))
# movie.append(input("enter your third favourite movie name :"))
# print(movie)

# Question 2
# WAP to check whether the given list is palindrome or not. A list is said to be palindrome if it reads the same from front and back. 
list1 = [1,2,1,4,5,4,3,2,1]   
list2 = [3,4,5,4,3]
copy_list1=list1.copy()
copy_list2=list2.copy()

copy_list1.reverse()
copy_list2.reverse()

if(copy_list1 == list1):
    print("palindrom")
else:
    print("not")

if(copy_list2==list2):
    print("palindrome")
else:
    print("not")

# Question 3

# tuple = ("C","D","A","A","B","B","A")
# print(tuple.count("A")) 


# list = ["C","D","A","A","B","B","A"]
# list.sort()
# print(list)

# list1 = [1,2,3,3,1]
# list1.reverse()
# if(list1 == [1,2,3,3,1]):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

###################################################################### THANK YOU #################################################################################################