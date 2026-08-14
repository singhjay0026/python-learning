#Store following words in the dictionary
# table : "a piece of furniture", "list of facts and figures"
# "cat" : "a small animal"

meaning = {
    "table" : "a piece of furniture, list of facts and figures", 
    "cat" : "a small animal", 
}

print(meaning)


#You are given a list of subjects for students. Asume one classroom is required for one subject. 
# How many classroom are needed by all student. 
#"python", "java", "c++", "python", "java", "javascript", "python", "java", "c++", "c"

subjects = {
   "python", "java", "c++", "python", "java", "javascript", "python", "java", "c++", "c"
}
print(len(subjects))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with a empty dictionary and add one by one.
# Use subject name as key and marks as value.

marks = {}

# x = int(input("Enter Physics Marks :"))
# marks.update({"Physics": x})
# x = int(input("Enter Chemistry Marks :"))
# marks.update({"Chemistry": x})
# x = int(input("Enter Maths Marks :"))
# marks.update({"Maths" : x})
# print(marks)


#Figure Out a way to store 9 and 9.0 as sep values in the set.

values = {9, "9.0"}       #WAY 1
print(values)


values = {"9", 9.0}           #WAY 2
print(values)

values = {
    ("float", 9.0), 
    ("int", 9)
}
print(values)