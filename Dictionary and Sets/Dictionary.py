info = { 
    "name" : "Apna College",
    "subjects" : ["python", "C", "Java"],
    "topics" : ("dict","sets"),
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.4
}

print (info)
print (type(info))
print (info["subjects"])
info["name"] = "Ajay"
info["surname"]  = "Singh"
print (info)

null_dict = {}
null_dict["name"] = "Jay"
print(null_dict)

student = {                     # NESTED DICTIONARY
    "name" : "Krishna",
    "subjects" : {
        "phy" : 99,
        "chem" : 97,
        "math" : 98 
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

# functions in Dictionary

print(student.keys())            #returns all Keys
print(list(student.keys()))      #type casting to list
print(student.values())          #returns all values
print(student.items())           #retuns all (key, val) pairs as tuples 
pairs = list(student.items())
print(pairs[0])
print(student.get("name"))       #returns the according to value
print(student.get("name2"))      #no error ---> NONE will be printed     
# print(student["name2"])          error
student.update({"city" : "delhi"})     #inserts the specified items to the dictionary
print(student) 


