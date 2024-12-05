# Approach 1 using for loop
mylist=[10,20,30,40,50,10,10]
x=10
count=0
for ele in mylist:
    if (ele==x):
        count=count+1
print("{}has occured {} times".format(x,count))

# Approach 2 using count()
mylist=[10,20,30,40,50,10,10]
x=10
print("{} has occured {} times".format(x,mylist.count(x)))

# Approach 3 using counter
from collections import Counter
mylist=[10,20,30,40,50,10,10]
x=10
dict=Counter(mylist)
print("{} has occured {} time".format(x,dict[x]))


