# To find the maximum element in the array
arr=[1,20,30,40]
max=arr[0]
n=len(arr)
for i in range(1, n):
    if arr[i]>max:
        max=arr[i]
print("Maximum number is: ",max)
# To find minimum element in the array
arr=[1,20,30,40]
min=arr[0]
n=len(arr)
for i in range(1, n):
    if arr[i]<min:
        min=arr[i]
print("Minimum number is: ",min)