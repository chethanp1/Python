# Approach 1
pattern=""
for i in range(1,6):
    if i%2==0:
        pattern +='H'
    else:
        pattern +='X'
    print(pattern)

# Approach 2
for i in range(1,6):
    for j in range(1,6):
        print("x", end=" ")
    print()
