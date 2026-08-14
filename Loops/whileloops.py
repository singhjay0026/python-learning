i = 1
while i <= 10:               # Stopping Condition
    print("Jay Singh", i)
    i += 1

# print Numbers from 1 to 5
i = 1
while i <= 5:                 # Stopping Condition
    print(i)
    i += 1
print("Loop Ended")

# print Numbers from 10 to 1
i = 10
while i >= 1:                    # Stopping Condition
    print(i)
    i -= 1

heroes = ["ironman", "thor", "superman", "batman"]
idx = 0 
while idx < len(heroes):    #Traverse - ek ke bad ek element ko check karna
    print(heroes[idx])
    idx += 1

# BREAK 
i = 1
while i <= 5:
    print(i)
    if(i==3):
        break
    i += 1
print("End Of Loop")

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 36
idx = 0
while idx < len(nums):
    if(nums[idx] == x):
        print("FOUND At IDX", idx)
        break
    else:
        print ("finding")
    idx += 1
print("End Of Loop")

# CONTINUE

i = 0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

#Print odd Numbers from 1 to 10

i = 1 
while i<=10:
    if(i%2 ==0):
        i+=1
        continue
    print (i)
    i+=1

#Print Even Numbers from 1 to 10

i = 1 
while i<=10:
    if (i%2 != 0):
        i+=1
        continue
    print (i)
    i+=1

