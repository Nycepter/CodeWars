"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once. """


def solution(number):
    """This function takes a number and adds all of the numbers between 1 and input number that are divisible cleanly by 3 or 5.

    Args:
        number (_int_): Number that is the end of the range.

    Returns:
        _int_: Sum off all the numbers pulled by the function.
    """
    sum = 0
    if number < 0:
        return 0
    else:
        for i in range(1, number):
            if i % 3 == 0 or i % 5 == 0:
                sum += i
    return sum
