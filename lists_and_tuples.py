#Lists in Python
list1 = [33.3, 44.5, 65.5, 88.9, 78.3]
print(list)
print(type(list))

list2 = ["habib", 23, "ahmed", 24, 55.5]
print(list2)
print(list2[0])
print(list2[1])
print(list2[2])

list2[1] = 22
print(list2)

#List Slicing
list = [1, 2, 3, 4, 5]
print(list[1:4])
print(list[:4])
print(list[0:len(list)])
print(list[:])

#List Methods
list = [1, 2, 3, 4, 5]
list.append(7)
print(list)

list = [2, 1, 4, 3, 5]
list.sort()
print(list)

list = [1, 2, 3, 4, 5]
list.sort(reverse=True)
print(list)

list = [10, 11, 13, 14, 15]
list.insert(2, 12)
print(list)

list.remove(10)
print(list)

list.pop(3)
print(list)

list = ["Habib", "Ahmed", "Ali", "Hameed", "Asghar"]
list.sort()
print(list)

#Tuples in Python
tup = (2, 2, 4, 1, 2, 2, 5)
print(type(tup))

#Tuples Methods
print(tup.index(4))
print(tup.count(2))
