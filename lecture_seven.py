######################################################### FILE input/output ####################################################################################################

# file i/o is used do operation in file like opening a file, reading a file, writing a file, closing a file , appending a file , editng a file etc.

# types of file :-
# 1. text file :- text file is a file which contains only text(character) data. text file is also called as ascii file. 
# EX:- .txt, .csv, .log, .xml, .json ,.docx , .pdf etc.

# 2. binary file :- binary file is a file which contains binary data. binary file is also called as non-ascii file.
# EX:- .jpg, .png, .gif, .mp3, .mp4, .avi, .exe, .dll etc.

# OPEN , READ & CLOSE FILE :-

# f = open("file.txt","r")                 # here , f is a file object which is used to perform operation on file. open() function is used to open a file. "file_txt" is the name of the file."r" is the mode in which we want to open the file. "r" mode is used to read the file. if the file is not present in the current directory then it will give error.)
# data = f.read()                          # read() function is used to read the entire content of the file.
# print(data)                              # print the data
# print(type(data))                        # data is a string type because read() function returns the data in string format.
# f.close()                                # close() function is used to close the file. it is a good practice to close the file after performing operation on it.

# f=open("demo.txt","r") 
# data = f.read()
# print(data)
# f.close()

# data = f.read()
# print(data)

# data =f.readline()
# print(data)
# f.close()                                        # yeh file ko close kar dega aur agar humne file ko close kar diya toh uske baad hum file ke andar koi bhi operation nahi kar sakte. isliye isko humesha last me hi use karna chahiye.
# agar hum pehle data =f.read() kar lenge toh uske baad jo pointer ke paas koi data nahi hoga . and agar hum read(6) ya readline() karenge toh terminal me blank ho jayega.kyuki system ne pehle hi sab dekh liya hai 
# isliye hume humesa pehle read(n) ya readline() etc . karna chahiye ( agr hume dekhna hai toh).

#WRITING FILE :-
# f = open("practs.txt","w")                         # w mode is used to overwrite the file. if the file is not present in the current directory then it will create a new file with the given name. if the file is already present in the current directory then it will overwrite the existing content of the file.
# f.write("this is a demo file")

# f=open("practs.txt","a")                             # a mode is used to add the content in the file from the end. if the file is not present in the current directory then it will create a new file with the given name. if the file is already present in the current directory then it will append the content in the existing content of the file.
# f.write("\n this is a demo file")
# f.close()

# agar hum koi bhi file ka naam likh ke open karenge to python us file ko create kar dega agar humne pehle ka hi us file ko folder me nahi banye the 
# f=open("intro.txt","w")
# f.write("hello world this is a view of rounak")

# f=open("intro.txt","a")
# f.write("\n this is a intro file of rounak")
# f.close()

# "r+" mode is used to read and ovrwrite the file. aur yeh starting me overwrite karta hai ,if the file is not present in the current directory then it will give error.

# "w+" mode is used to write and read the file. if the file is not present in the current directory then it will create a new file with the given name. if the file is already present in the current directory then it will overwrite the existing content of the file and then read the content of the file.

# "a+" mode is used to append and read the file. if the file is not present in the current directory then it will create a new file with the given name. if the file is already present in the current directory then it will append the content from the endin the existing content of the file and then read the content of the file.

# f=open("demo.txt","r+")
# f.write("hello world")
# print(f.read())
# f.close()

# f=open("practs.txt","w+")
# f.write("hello world this is a demo file of jatayu")
# print(f.read())
# f.close()

# f=open("demo.txt","a+")
# f.write("\n this is a business owner")
# f.seek(0)                                 # yeh pointer ko start me laata hai.
# print(f.read())                           # yeh kuch bhi nahi show karega kyuki humne niche append karwaya hai aur poointer end me hai isliye read() function kuch bhi nahi show karega. agar humne f.seek(0) use kiya hota to yeh poora content show karta.
# f.close()

# with open("demo.txt","a+") as f:                      # with statement is used to open the file and it automatically closes the file after performing operation on it. it is a good practice to use with statement to open the file.
#     f.write("\n i am rounak asheesh mishra")
#     data = f.read()
#     print(data)
# with open("practs.txt","w+") as f:
    # f.write("hello world , here is raunak the conqueror of world with ram ji")
    # print(f.read())

# import os                                             # os is prebuilt ptython module which is used to delete the file from the directory. os.remove() function is used to delete the file from the directory.
# os.remove("demo.txt")

# Q1:- Create a new file "pract.txt" usinig python.add the following data in it:
with open("pract.txt","w") as f:
    f.write(" hi everyone \n we are learning FileI/O \n using java. \n I like programming in java")

with open("pract.txt","r") as f:
    data = f.read()
    print(data)

# Q2:- WAF that replace all occurances of " java" with "python" in above file.

# new_data = data.replace("java","python")               # yeh replace() function hai jo ki string ke andar ke word ko replace kar deta hai. isme pehla argument wo word hai jo hum replace karna chahte hai aur dusra argument wo word hai jo hum replace karna chahte hai.
# print(new_data)

# with open("new_pract.txt","w") as f:
#     f.write(new_data)

# Q3:- find learning word in the pract.txt file.

# word = "learning"
# with open("pract.txt","r") as f:
#     data =f.read()
#     if word in data :                                  # here in operator is used to check whether the word is present in the data or not. if the word is present in the data then it will return True otherwise it will return False.
#         print("Found learning ")
#     else:
#         print("not found")

# WAF to find in whihc line of the file does the word "learning: occure first .
def ckeck_linenumber():
    word="learning"
    data =True
    line_number=1
    with open("pract.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("found in :", line_number)
                line_number+=1
                return line_number

    return -1

print(ckeck_linenumber())

# Q 5:- from a file containing numbers seperated by comma,print the count od even numbers.
# with open("practs.txt","w") as f:
#     f.write("1,2,78,67,89,90,101,123")

# count=0
# with open("practs.txt","r") as f:
#     data = f.read()

#     nums =data.split(",")
#     for value in nums:
#         if (int(value)%2==0):
#             print(value)
#             count+=1

# print(count)

#################################################################### end ###################################################################



    




    











