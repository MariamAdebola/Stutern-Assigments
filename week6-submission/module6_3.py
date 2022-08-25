import numpy as np

# array of numbers btw 1 and 100
num = [*range(1, 101)]
print(num)

# generate even numbers within the array
even_num = np.array([*filter(lambda x: x%2 == 0, num)])
print(even_num)

# generate lcm of the even numbers
lcm_num = np.lcm.reduce(even_num)
print(lcm_num)
