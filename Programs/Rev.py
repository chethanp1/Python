# Using WHILE loop
num=int(input('Enter the number : '))
rev_num = 0
while num != 0:
 digit = num % 10
 rev_num = rev_num * 10 + digit
 num //= 10
print("After Reverse the Number is: " ,rev_num)