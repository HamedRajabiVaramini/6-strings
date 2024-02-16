'''
simple_programming_

This code uses format function
'''
s1 = "Simple Programming {}"
s2 = "is cool!"
print(s1.format(s2)) # Simple Programming is cool!

s3 = "Pi is {}"
result = 3.14
print(s3.format(result)) # Pi is 3.14

# Using more than one argument
s4 = "My name is \"{} {}\""
firstName = "Hamed"
lastName = "Rajabi"
print(s4.format(firstName, lastName))

# Using index for ordering the arguments
s4 = "My name is \"{1} {0}\""
firstName = "Hamed"
lastName = "Rajabi"
print(s4.format(lastName, firstName))

