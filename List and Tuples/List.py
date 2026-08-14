# LIST

marks = [94.4, 87.7, 92.5, 90.6, 85.8]
print (marks)
print(type(marks))
print (marks[:4])           # list Slicing 
print (marks[-3:-1])        # Ending Index is not included

student = ["Krishna", 99.7, 724, "Uttarpradesh"]
print (student[0])
student[0] = "Aryan"        # list are MUTABLE But String are IMMUTABLE
print (student)

list = [2, 1, 3]
list.append(4)              # Add One Element at the END
print (list)

list = [2, 1, 3]
list.sort()                 # It will sort in Ascending Order
print (list)

list = [2, 1, 3]
list.sort(reverse = True)   # It will sort in Descending Order
print (list)

list = [2, 1, 3]
list.reverse()              # reverses list
print (list)

list = [2, 1, 3]
list.insert(1,5)            # Insert element at index
print (list)

list = [2, 1, 1, 4, 5, 3]
list.remove(1)              # Remove first Occurance of element
print (list)

list = [6, 7, 2, 1, 3]
list.pop(0)                 # Remove element at Index
print (list)