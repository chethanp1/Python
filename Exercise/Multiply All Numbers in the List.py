#  Approach 1 using for loop
mylist=[2,2,4,6]
result=1

for x in mylist:
    result=result * x
print("Multiplication value is : ", result)


#Approach 2 using numpy
import numpy
mylist = [2, 2, 4, 6]
result=numpy.prod(mylist)
print(result)
