for i in range(10):           #range(stop)
    print(i)

for i in range(2, 10):       #range(start, stop)
    print(i)

for i in range(2, 10, 2):     #range(start, stop, step)
    print(i)

#print even no from 1 to 1000
for i in range(2, 1000, 2):
    print(i)

#Practice problem'

#Print no from 1 to 100 
for i in range(1, 101):
    print(i)


#Print no from 100 to 1
for i in range(100, 0, -1):
    print(i)

#Print the multiplication table of n

n = int(input("Enter number :"))
for i in range(1, 11, 1):
    print(n*i)

#Pass Terminology
for i in range(5):
    pass 
if i > 5:
    pass
print("Some Usefull Work")

#WAP to find the sum of first n natural numbers (Using For Loop)

n = int(input("Enter Number : "))
sum = 0
for i in range(1, n+1):
    sum += i
print("Total Sum =",sum)

#WAP to find the sum of first n natural numbers (Using while Loop)


n = int(input("Enter Number : "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Total Sum =",sum)

#WAP to find the factorial of first n natural no (Using For Loop)

n = int(input("Enter Number : "))
fact = 1
for i in range(n, 0, -1):
    fact *= i
print("Factorial =", fact )

       #OR         #OR         #OR

n = 5
fact = 1
for i in range(1 , n+1):
    fact *= i
print("Factorial =", fact )

#WAP to find the factorial of first n natural no (Using while Loop)

n = int(input("Enter Number : "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial =", fact )


#aur ek diff notice karna dono loop ke question solve mein 
# 
# while i += 1
# for mein nhi rahega  i += 1
#  