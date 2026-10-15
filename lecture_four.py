##################################################### dictionay & sets in python ####################################################################################

# Dictionary is a collection of key value pairs. It is unordered, mutable and indexed. In python dictionaries are written with curly brackets, and they have keys and values.
# #
# info = {
#     "name" : "ronak",
#     "age" : 19,
#     "name2" : "ronak mishra",
#     "caste" : "brahmin",
#     "is_student" : True,
#     "list" : [1,2,3,4,5],
#     "tuple" : (1,2,3,4,5),
#     12 : 234                            # this is also valid key in dictionary
# }
# print(info)
# print(type(info))
# print(info[12])
# info["jatayu"] = "parrot"               # this is how we can add new key value pair in dictionary
# info["age"] = 20                        # this is how we can update the value of existing key in dictionary
# print(info) 

# dict = {}                               # we can also create empty dictionary in python by using curly brackets
# # or both are same              
# dict = {

# }
# dict["name"] = " apna collage"
# dict["surname"] = " kumar"

# student = {
#     "name" : "rounak mishra",
#     "subject" : {
#         "math":78,
#         "science":99,
#         "marathi":11,
#         "urdu":1,
#         "Awadhi":100,
#         "English":100,
#         "Kazakistani bhasa":100,
#         "nepali bhasa":1,
#     },
#     "school":"Atankwadi public school karachi pakistan",
#     "role on pakistan":"on mission to destory pakistan",
# }
# print(student)
# print(student["school"])
# print(student["subject"]["Awadhi"])
# # print(list(student.keys()))           # this will print all the keys of dictionary
# print(tuple(student.keys()))            # this will print all the keys of dictionary as a tuple
# print(list(student.values()))           # this will print all the values of dictionary
# print(list(student.items()))            # this will print all the key value pairs of dictionary
# pair = list(student.items())            # this is how we can convert dictionary into list of key value pairs
# print(pair)          
# print(pair[0])                          # for accessing the first key value pair of dictionary
# print(pair[1])

# print(student["name"])                  # for this hum dono method ko use kar sakte hai but
# print(student.get("name"))
# print(student["name2"])                 # this will give error & iska nuksan yeh hoga ki agar hum aisa code likh dete hai toh 
#                                          iske niche ke jitne bhi code likhe hue honge woh sare me error aa  jayega isliye hum get() ka use karte hai 

# print(student.get("name2"))             # this will give None because name2 key is not present in dictionary
# student.update({"surname": "kumar"})    # this is how we can add new key value pair in dictionary
# print(student)
# student.update({"name":"ronak mishra kumar"})           # this will update ho jayega pehle wale key value ko replace karke 
# print(student)

######################################################## SETS IN PYHTON ##################################################################################################

# collection = {1,2,3,4,4,'hellow world',12}              # it written in curly brackets but it is not a dictionary because it does not have key value pair. It is unordered, mutable and unindexed. It does not allow duplicate values.
# print(type(collection))                                 # iske andar int , float , string , boolean , tuple store karte hai but list & dictionary nahi store karte hai (kyuki woh immutable hote hai)!!
# print(collection)
# print(len(collection))                                  # total numbmer of items in set
# collection = {}                                         # yeh dictionary hai kyuki aisa empty varible sirf dictionary ke liye hi valid hai. Set ke liye aisa empty variable valid nahi hai
# print(type(collection))                        

# collection = set()                                      # yeh right way hai empty set create karne ka
# #print(type(collection))

# collection.add(2)
# collection.add("jatayu")
# print(collection)

# collection.remove(2)
# collection.add(("hello world","hello everyone"))        # this is how we can add tuple in set
# collection.add("hello")

# collection2 =collection.copy()                          # this is how we can copy the set into another set
# print(collection2)

# collection.clear()                                      # this is how we can clear the set
# print(collection)

# collect = { " hellow world "," hellow ram "," hellow shiv "," raunak mishra "}
# collect.pop()                                           # idhar koi bhi value randomly pop ho jata hai kyuki set me index nahi hota hai
# print(collect)

# set1 = {1,2,3}
# set2 = {3,4,5}                                            
# print(set1.union(set2))                                 # this is how we can combine two sets and remove the duplicate values from both sets
# print(set2.union(set1))
# print(set2.intersection(set1))                          # this is how we can find the common values from both sets
# print(set1.intersection(set2))                          # this is how we can find the common values from both sets

# Question 1
# dict = {
#     "table":("a piece of furniture "," list of facts & figures "),
#     "cat": " a small animal ",
# }
# print(dict)

# Question 2
# subjects = {"python","java","c++","python","javascript","java","python","java","c++","C"}
# print(len(subjects))      # 

# Question 3
marks = {}
marks["chemistry"] = int(input("enter your chemistry marks :"))
marks["physics"] = int(input("enter you physics marks :"))
marks["Maths"] =int(input("Enter your maths marks :"))
# math = int(input("enter your math marks :"))
# marks.update({"math":math})
# print(type(marks["math"]))
print(marks)

# Question 4
# Figure out a way to store 9 and 9.0 as separate values in the set. 
#(You can take help of built-in data types.)??

# value = { 9,9.0}                                        # python me 9 aur 9.0 ko same value ke roop me treat karta hai isliye dono ko alag alag store karne padta hai
# print(value)

# value = {9,"9.0"}                                       # isme hum 9.0 ko string me convert kar ke alag alag store kar sakte hai
# print(value) 
#  #or 
# value = {"9",9.0}                                        # aur hum 9 ko bhi string me convert kar ke alag alag store kar sakte hai jisse 9.0 automatically alag alag store ho jayega
# print(value)

# #or by built-in data types
# value = {("float",9.0),("int",9)}
# print(value)
# #0r 
# value = {
#     ("float",9.0),
#     ("int",9)
# }
# print(value)  
 
###################################################################### THANK YOU #################################################################################################