#light = "blue"
    
#if (light == "red"):    # if dtatement saare condition ko check karta h
#    print ("stop")
#elif (light == "green"):  # elif tabhi check hoga jab "if" statement will be false
#    print ("go")           # agar if ka statement pehle he true hogya toh elif will not checked
#elif (light == "yellow"):
#    print ("look")
#else:
#    print ("light is broken")

#print ("end of code")

#num = 5

#if (num > 2):
#    print ("greater than 2")  #indentation = those 4 spaces in starting

#elif (num > 3):
#    print ("greater than 3")

marks = 84

if (marks >= 90):
    grade = "A"
elif (marks >= 80 and marks < 90):
    grade = "B"
elif (marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student is", grade)


marks = int(input("Enter Students Marks : "))

if (marks >= 90):
    grade = "A"
elif (marks >= 80 and marks < 90):
    grade = "B"
elif (marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student is", grade)

age = 20
# nesting
if(age >= 18 ):
    if (age >= 80):
        print ("Cannot Drive")
    else: 
        print ("Can Drive")
    