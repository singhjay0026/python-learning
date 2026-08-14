# concatenation

str1 = "This is a string.\nWe are creating it in python." # \n = it will start a sentence from a new line 
print (str1)

str2 = "JAY" 
str3 = "SINGH" 
final_str = print(str2+str3)

# length of str

str2 = "JAY" 
print (len(str2))

str3 = "SINGH"
print (len(str3))

final_str = str2 + " " + str3 # " " - empty string = ye add karne par bhi isse ek character count karega computer
print (final_str)
print (len(str2+str3))

# Indexing

str = "JAY_SINGH" # index humesha 0 se start hota h
ch = str[0]
print (ch)

# Slicing       str[starting_index : Ending_index] Ending index is not included
str = "caterpillar"
print (str[:4])   # [0:4]
print (str[4:8])   # [4:len(str)]

str = "Rajputana"
print (str[-5:-1])  # peeche se numering -1 se start hoga

# string function
str = "i am studying python from Apna College"
print (str.endswith("ege"))                   #returns true if string ends with substr
print (str.replace("python", "Javascript"))   #replaces all occurance of old value in NEW
print (str.capitalize())                      #capitalizes 1st character
print (str.find("o"))                         #returns first index of first occurance
print (str.count("from"))                     #counts the occurences of substr
