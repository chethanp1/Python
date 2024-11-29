# Approach 1- simple swap of two elements in list

mylist=[10,20,340,45]
print(mylist)
pos1,pos2 =1,3
mylist[pos1], mylist[pos2]=mylist[pos2], mylist[pos1]
print(mylist)

# Approach 2 - using  pop method
mylist=[12,34,566,67]
print(mylist)
pos1,pos2=1,3
first= mylist.pop(pos1)  #34
second=mylist.pop(pos2-1) # 12,566,67
mylist.insert(1, second)
mylist.insert(3,first)
print(mylist)

# Approach 3 using tuple
mylist=[12,234,4,45]
print(mylist)
pos1,pos2=2,3
get=mylist[pos1],mylist[pos2]
mylist[pos2],mylist[pos1]=get
print(mylist)



