#=====================
#Ways to Write Strings
#=====================
str1 = 'hello how are you'
str2 = "hello how are you"
str3 = """hello how are you"""
print(str1)
print(str2)
print(str3)

str4 = 'My name is "Habib"'
print(str4)
str5 = "This is Python's tutorial"
print(str5)

#========================
#Concatenation of Strings
#========================
str1 = "Habib"
str2 = "Ahmed"
con = str1 + " " + str2
print(len(con))
print(con)

print("My name is habib ahmed \nmy age is 23")
print("My name is habib ahmed \tmy age is 23")

#=====================
#Indexing in Python
#=====================
str = "Habib"
idx = str[3]
print(idx)

#=====================
#Slicing in Python
#=====================
name = "HabibAhmed"
print(name[5:8])
print(name[:len(name)])
print(name[5:])

fruit = "apple"
print(fruit[-4:-1])

str = "my name is Habib Ahmed"
print(str.endswith("mad"))
print(str.capitalize())
print(str.replace("Ahmed","Ullah"))
print(str.find("is"))
print(str.count("i"))
