# Approach 1 using slice operator
mylist=[10,20,30,40,50]
mylist_copy=mylist[:]
print(mylist_copy)

# Approach 2 using extend method
mylist=[10,20,30,40,50]
mylist_copy=[]
mylist_copy.extend(mylist)
print((mylist_copy))

# Approach 3 using list method
mylist=[10,20,30,40,50]
mylist_copy=list(mylist)
print((mylist_copy))

# Approach 4 using copy method
mylist=[10,20,30,40,50]
mylist_copy= mylist.copy()
print(mylist_copy)

# Approach 5 using list comprehension
mylist=[10,20,30,40,50]
mylist_copy=[i for i in mylist]
print(mylist_copy)
