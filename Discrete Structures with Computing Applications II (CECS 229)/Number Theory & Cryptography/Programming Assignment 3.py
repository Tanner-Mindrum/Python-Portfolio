from math import gcd

# Chinese Remainder Theorem (See Theorem 2 of Section 4.4):
# Write a function that will take in two list inputs: aList and mList.
# aList will contain the list of a values and mList will contain the list of m values.
# Your function should then provide the final x value after it has been modded by m.
# The x value should be returned as an integer.
def relatively_prime(L):
    for i in range(len(L)):
        for j in range(i + 1,len(L)):
            if gcd(L[i], L[j]) != 1:
                return "Not Pairwise Relatively Prime"
    return "Pairwise Relatively Prime"

def chinese_remainder_theorem(a_list, m_list):
    m = 1
    M = 1
    y_count = 1
    M_list = []
    y_list = []
    x = 0

    if len(a_list) != len(m_list):
        return "Lists are not of the same length!"

    for i in range(len(m_list)):
        if (m_list[i] <= 1):
            return "Cannot proceed, mList input not pairwise relatively prime"

    if relatively_prime(m_list) != "Pairwise Relatively Prime":
        return "Cannot proceed, mList input not pairwise relatively prime"

    else:
        for i in range(len(m_list)):
            m *= m_list[i]

        for i in range(len(m_list)):
            M_list.append(m // m_list[i])

        for i in range(len(m_list)):
            while True:
                if (M_list[i] * y_count % m_list[i] != 1):
                    y_count += 1
                else:
                    break
            y_list.append(y_count)

        for i in range(len(m_list)):
            x += (a_list[i] * M_list[i] * y_list[i])
        x %= m

    return x
