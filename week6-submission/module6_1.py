#import numpy
import numpy as np

# get arange of integer numbers from 5.5 to 20.5
num = [int(i) for i in np.arange(5.5, 21.5)]
print([*(num)])
print(len(num))

# get the count of odd numbers of the list of integers created
odd_num = [*filter(lambda i: (i%2 != 0), num)]
print(len(odd_num))

# get the count of even numbers of the list of integers created
even_num =[*filter(lambda i: (i%2 == 0), num)]
print(len(even_num))

# square and cube every number in the list
new_num = [*map(lambda x: (x, x*x, x*x*x), num)]
print(new_num)
