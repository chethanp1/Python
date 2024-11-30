# # Searching element in the list
mylist=[1,23,4,5,65]
ele=1
flag=0

for i in mylist:
    if (i==ele):
        print("Element Found")
        flag=1
        break
if(flag==0):
    print("Item not found")

# Approach 2 using in function
mylist=[1,2,3,4,45]
ele=3
if (ele in mylist):
    print("Element Found")
else:
    print("Element Not Found")
    z