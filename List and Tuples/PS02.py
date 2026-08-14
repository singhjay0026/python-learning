# WAP to ask the user to enter 3 of their favorite movies and store them in a list?

movies = []
movies.append(input("Enter 1st Movie : "))
movies.append(input("Enter 2nd Movie : "))
movies.append(input("Enter 3rd Movie : ")) 
print(movies)

#WAP to check if a given list is a palindrome or not?
list1 = ["m", "a", "a", "m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("NOT a Palindrome")


grades = ["C", "D", "A", "A", "B", "B", "A"]
print(grades.count("A"))
grades.sort()
print(grades)