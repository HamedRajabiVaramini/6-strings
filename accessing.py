'''
simple_programming_

This code defines a string and 
tries to access to the characters or 
substring of it
'''
s1 = "Python Language"

s2 = s1[0] # s1 is the first character: "P"
s3 = s1[5] # s2 is "n"
s4 = s1[6] # s3 is " " (space)

# starts from 0 (inclusive) 
# and stops at 6 (exclusive)
s5 = s1[0:6]  
print(s5) # prints "Python"

# Iterating over characters 
for c in s1: 
    print(c)

