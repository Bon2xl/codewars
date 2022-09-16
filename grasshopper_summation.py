# Grasshopper - Summation
# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

def summation(num):
    total = 0

    if (num == 1):
        return num

    for n in range(1, num+1):
        total += n

    return total;
    


# test.assert_equals(summation(1), 1)
print(summation(8));