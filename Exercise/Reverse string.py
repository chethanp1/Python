# Approach 1
# str=input("Enter the String: ")
# words=str.split()
# words=words[::-1]
# outputstr=' '.join(words)
# print(outputstr)

# Approach 2
str=input("Enter the string")
rev_str=" "
for char in str:
    rev_str=char+rev_str
print(rev_str)