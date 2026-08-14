# STRINGS

#WAP to input users first name and print its length??
name = input("Enter Your Name : ")
print ("length Of Your Name is", len(name))

#WAP to find the occurence of $ in a string??
str = "Hi, $I am the $ symbol $99,99"
print(str.count("$"))

# CONDITIONAL

#WAP a program to check if a number entered by the user is odd or even??
num = int(input("Enter a Number :"))

if(num % 2 != 0):
    print("Odd Number")
else:
    print("Even Number")


a = 34
b = 40
c = 56
if (a > b and a > c):                        # a is not greater no
    print ("Greater Number is :", a)
elif (b > c ):
    print ("Greater Number is :", b)
else:
    print ("Greater Number is :", c)

#WAP to find the largest of 3 numbers entered by the user??
a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))
if (a >= b and a >= c):
    print ("First Number is Largest", a)
elif (b >= c):
    print ("Second Number is Largest", b)
else:
    print ("Third  Number is Largest", c)


#WAP a program to check if a number is a multiple of 7 OR not??
num = int(input("Enter a Number :"))
if (num % 7 == 0):                     # % - Remainder
    print ("It is Multiple of 7")
else:
    print ("It is not Multiple of 7")
