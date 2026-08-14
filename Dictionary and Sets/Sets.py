collection = set()         #empty set ; syntax
print(type(collection))

a = {1, 2 ,2 ,2 ,"hello", "world", "world", 4}
print(a)
print(len(a))        #total no of items

#set Methods

b = set()
b.add(5)
b.add(7)
b.add(26)
print(b)
# b.remove(5)
# print(b)
# b.clear()              #empty set
# print(b)
b.pop()
print(b)

c = {"hello", "python", "world", "coding","apna college"}
print(c.pop())
print(c.pop())            #it will pop out random value

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))
print(set1.intersection(set2))
