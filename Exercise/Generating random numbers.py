# Approach 1 using random inbuilt module

# Float

# Float  numbers between 1 to 100
import random
random_no=random.random()
print(random_no)

# Float number in specified range
import random
random_no=random.uniform(1,100)
print(random_no)

# To print Integer Interger
random_no=random.randint(1,100)
print(random_no)

# To print even number in range
random_no=random.randrange(0,100,2)
print(random_no)

# To print random range of numbers
random_no=random.sample(range(0,100),3)
print(random_no)