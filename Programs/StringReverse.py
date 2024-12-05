# Approach 1 with reverse() method
mylist=[20,30,40,50]
print("List before reversing :",mylist)
mylist.reverse()
print("List after reversing :",mylist)

# Approach 2 using slice operator
mylist=[20,30,40,50]
print("List before reversing :",mylist)
mylist2=mylist[::-1]
print("After Reversing:", mylist2)