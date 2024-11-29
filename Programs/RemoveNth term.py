# Checking Nth term of repeating word in list
mylist=["YES", "No","YES"]
word="YES"
n=2

count=0
for i in range(0,len(mylist)):
    if mylist[i]==word:
        count=count+1
        if (count==n):
            del mylist[i]
print("Updated list: ",mylist)