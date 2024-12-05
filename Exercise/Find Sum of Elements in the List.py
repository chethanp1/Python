# Approach 1 using for loop
mylist=[10,20,30,40,50,10,10]
total=0
for i in range(0,len(mylist)):
    total=total+mylist[i]
print("Sum is :",total)

# Approach 2 using sum function
mylist=[10,20,30,40,50,10,10]
total=sum(mylist)
print("Sum is :", total)