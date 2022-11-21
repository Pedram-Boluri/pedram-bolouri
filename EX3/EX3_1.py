def EX3_1(x):
    '''
    (int) -> int

    This is "The Collatz Conjecture" function.
        This function will return the amount of steps it takes for any
        positive integere to reach "1" acording to "The Collatz Conjecture."

        For example:

            >>>EX3_1(2) ➞ 1
            >>>EX3_1(3) ➞ 7
            >>>EX3_1(10) ➞ 6
    '''
    steps = 0
    while x > 1:
        if x % 2 == 0:
            x = x/2
            steps += 1
            if x == 1:
                break
        else:
            x = x*3 + 1
            steps += 1
    return(steps)
