# Write code to print
# X
# Hx
# Hx
# Xhxh
# HxhxH
pattern = ""
for i in range(1, 6):
    if i % 2 == 0:
        pattern += "H"
    else:
        pattern += "X"
    print(pattern)
