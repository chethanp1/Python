# Approach 1 using temp variable
mylist=[1,2,23,4,5]
print(mylist)
size=len(mylist)

temp=0
temp=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp

print("my list after swapping:",mylist)

# Approach 2 using index
mylist=[1,2,3,4,5]
print(mylist)
mylist[0],mylist[-1]=mylist[-1],mylist[0]
print(mylist)

# Approach 3
mylist=[1,2,4,5,6]
print(mylist)
# Using tuple and packing
get=(mylist[0],mylist[-1])
#  Unpacking
mylist[-1],mylist[0]=get
print(mylist)

# Approach 4
# Using * Operand
mylist=[1,2,3,5,6]
print(mylist)
start,*middle,end=mylist
mylist=[end,*middle,start]
print(mylist)

# Approach 5
# Using pop method
mylist=[1,2,3,4,5]
print(mylist)
first=mylist.pop(0)
last=mylist.pop(-1)
mylist.insert(0,last)
mylist.append(first)
print(mylist)

