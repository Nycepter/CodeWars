"""Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0."""

"""
def summation(num):
    total = 0
    for i in range(1, num + 1):
        total += i
        return total
"""


def summation(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    print(total)


summation(int(input("Enter number here \n")))
