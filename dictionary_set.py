#====================
#dictionary in Python
#====================
info = {
    "name" : "Habib",
    "age" : 23,
    "subjects" : ["Java", "Python", "C++"],
    "is_adult" : True,
    "education" : ("intermediate", "Bachelors")
}

print(info)
print(info['subjects'])
info['name'] = "Ahmed"
info['surname'] = "Ali"
print(info)

#================
#Empty dictionary 
#================
null_dict = {}
null_dict["name"] = "Habib"
print(null_dict)

#=================
#nested dictionary
#=================
dict = {
    "name" : "Habib",
    "subjects" : {
        "phy" : 40,
        "chem" : 44,
        "math" : 45
    }
}
print(dict)
print(dict["subjects"])
print(dict.keys())
print(list(dict))
print(len(list(dict)))

#==================
#Dictionary Methods
#==================
data = {
    "name" : "Habib",
    "sub" : {
        "phy" : 44,
        "chem" : 40,
        "math" : 45 
    }
}
#return all keys 
print(data.keys())
#return all values
print(data.values())
#return all key & values as tuples
new = list(data.items())
print(new[0])
print(new)
#return the key according to value
print(data.get("name"))
#insert the specifind items to the dictionary
age = {
    "myage" : 23,
}

data.update(age)
print(data)

#=============
#Set in Python
#=============
collection = {1, 2, 2, 2, "hello", "world", "world"}
print(collection)
print(type(collection))
print(len(collection))

#=========
#Emply set
#=========
math_set = set()
print(type(math_set))

#===========
#Sets Method
#===========
collection1 = set()
collection1.add(1)
collection1.add(2)
collection1.add(3.3)
collection1.add("Habib Ahmed")
collection1.add((1,2))

collection1.remove(3.3)

collection1.pop()

print(collection1)
print(len(collection1))
print(type(collection1))

#====================
#Union & intersection
#====================
set1 = {1, 2, 3}
set2 = {3, 4, 5}
uniset = set2.union(set1)
print(uniset)

interset = set1.intersection(set2)
print(interset)
