# CECS 229: Programming Assignment 1
# Sections covered: 4.1, 4.2

# Question 1
# Write a Python expression to find the number of seconds in a decade. You can assume one year
# has 365 days. Save the value to a variable called seconds_in_decade.
seconds_in_decade = 60 * 60 * 24 * 365 * 10

# Question 2
# Write a Python expression to find the remainder of 5789248 divided by 14 by using Python’s
# modulus operator. Save the value to a variable called remainder_with_mod.
remainder_with_mod = 5789248 % 14

# Question 3
# Write a Python expression to find the remainder of 5789248 divided by 14 without using
# Python’s modulus operator. Instead, you must use the // operator. Save the value to a variable
# called remainder_without_mod.
remainder_without_mod = 5789248 - 5789248 // 14 * 14

# Question 4
# Write a comprehension over {2, 4, 6, 8, 10} whose value is the set consisting of their cubes
# minus 1.
{(x**3 - 1) for x in {2,4,6,8,10}}

# Question 5
# Write a comprehension over [1, 2, 3, 4, 5] whose value is the list consisting of the squares minus
# the value’s index. Assume that the index starts at zero. 
M = [1,2,3,4,5]
[(y**2 - M.index(y)) for y in M]

# Question 6
# Write a Python expression that will give the intersection of the following two sets:
# First Set: the square of numbers from 1 to 30.
# Second Set: the doubling of numbers from 1 to 30
{(a**2) for a in range(1, 31)} & {(b*2) for b in range(1, 31)}
