"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 1000 and 2000 (both included).

The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
def filterNumber(a,b):
    numbers=[];
    for x in range(a,b+1):
        if x % 7 == 0 and x % 5 != 0:
            numbers.append(x)
    print(numbers)


filterNumber(1000,2000)