#================
# Lists in Python
#================
list1 = [33.3, 44.5, 65.5, 88.9, 78.3]
print(list1)
print(type(list1))

list2 = ["habib", 23, "ahmed", 24, 55.5]
print(list2)
print(list2[0])
print(list2[1])
print(list2[2])

list2[1] = 22
print(list2)

#============
#List Slicing
#============
list3 = [1, 2, 3, 4, 5]
print(list3[1:4])
print(list3[:4])
print(list3[0:len(list3)])
print(list3[:])

#=============
# List Methods
#=============
list4 = [1, 2, 3, 4, 5]
list4.append(7)
print(list4)

list5 = [2, 1, 4, 3, 5]
list5.sort()
print(list5)

list6 = [1, 2, 3, 4, 5]
list6.sort(reverse=True)
print(list6)

list7 = [10, 11, 13, 14, 15]
list7.insert(2, 12)
print(list7)

list7.remove(10)
print(list7)

list7.pop(3)
print(list7)

list8 = ["Habib", "Ahmed", "Ali", "Basharat", "Fareed"]
list8.sort()
print(list8)

#=================
# Tuples in Python
#=================
tup = (2, 2, 4, 1, 2, 2, 5)
print(type(tup))

#===============
# Tuples Methods
#===============
print(tup.index(4))
print(tup.count(2))
