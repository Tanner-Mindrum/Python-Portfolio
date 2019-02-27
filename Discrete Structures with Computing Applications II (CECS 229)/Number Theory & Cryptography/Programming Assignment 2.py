import math

# Question 1
# Write afunction that will take in three inputs: base, exponent, and divisor. The output would be the values of the
# modulus operations such that when multiplied and then taken the modulus of the divisor, you will get the problem’s
# remainder. The output should bea list data type.

def modulus(base, exponent, divisor):
    binary_nums = []
    exponentiation_nums = []
    result_nums = []
    
    while exponent > 0:
        binary_nums.append(exponent % 2)
        exponent = exponent // 2
        
    for i in range(len(binary_nums)):
        exponentiation_nums.append(base ** (2**i) % divisor)
        
    for i in range(len(binary_nums)):
        if binary_nums[i] == 1:
            result_nums.append(exponentiation_nums[i])
            
    print(result_nums)

# Question 2
# Write a function that will take in a list of integers and then output whether the list is pairwise relatively prime.
# If the list is pairwise relatively prime, then the function will output “Pairwise Relatively Prime”.
# Otherwise, it will output “Not Pairwise Relatively Prime”.

def relativelyPrime(aList):
    ifPrime = []
    result = "Pairwise Relatively Prime"
    
    for i in range(len(aList) - 1):
        for j in range(i + 1, len(aList)):
                ifPrime.append(math.gcd(aList[i], aList[j]))
                
    for i in range(len(ifPrime)):
        if ifPrime[i] != 1:
            result = "Not Pairwise Relatively Prime"

    print(result)
