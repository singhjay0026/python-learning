# Print Numbers from 1 to 100
i = 1 
while i <= 100:
    print(i)
    i += 1

# Print numbers from 100 to 1
i = 100
while i >= 1:      # Stopping Condition
    print(i)
    i -= 1

# Print the Multiplication table of a Number 5
i = 1
while i <= 10:
    print(3*i)
    i += 1
    
# Print the elements of the following list using a loop:
#    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

idx = 0
while idx < len(nums):
    print(nums[idx])  # nums[0], nums[1], nums[2],..
    idx += 1

heroes = ["ironman", "thor", "superman", "batman"]
idx = 0 
while idx < len(heroes):    #Traverse - ek ke bad ek element ko check karna
    print(heroes[idx])
    idx += 1

# Search for the number X in this tuple using a loop:
#    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36
idx = 0
while idx < len(nums):
    if(nums[idx] == x):
        print("FOUND At IDX", idx)
    else:
        print ("finding....")
    idx += 1
print("End Of Loop")


# Print the elements of the following list using a loop:
#    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
for num in tup:
    print(num)

# Search for the number X in this tuple using a loop:
#    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49 )

x = 49
idx = 0
for num in tup:
    if (num == x):
        print ("Number Found at idx",idx)
    idx += 1

x = 49
idx = 0
for num in tup:
    if (num == x):
        print ("Number Found at idx",idx)
        break 
    idx += 1


