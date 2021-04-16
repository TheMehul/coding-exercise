#!/usr/bin/python3

import random

def countNums(nums, x):
    over = 0
    under = 0
    for num in nums:
        if num < x:
            under += 1
        elif num > x:
            over += 1
    print(f"above: {over}, below: {under}")

def rotateString(token, x):
    temp = token[len(token)-x:]+token[0:len(token)-x]
    print(temp)



nums  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
x = 5
print(f"nums: {repr(nums)}, x: {x}")
countNums(nums, x)

nums = []
for x in range(0,10):
    nums.append(random.randrange(1,10))
x = random.randrange(1,10)
print(f"nums: {repr(nums)}, x: {x}")
countNums(nums, x)


token = "Testing123"
x = 12
print(f"\ninput: '{token}', rotate {x}")
rotateString(token, x)

token = "Testing123"
x = random.randrange(1,len(token))
print(f"input: '{token}', rotate {x}")
rotateString(token, x)
