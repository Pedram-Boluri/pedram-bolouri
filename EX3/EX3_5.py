def EX3_5(List):
    '''
    (list) -> bool
    
        This is the "25-Mile Marathon" function. 
        Given the length of each portion of the marathon track, this function will
        return True if the track is exactly 25 miles, otherwise False.
        Note: Negative integers are going to be converted into positive integers.
        
        Examples:
            EX3_5( [1, 2, 3, 4] ) ➞ False
            EX3_5( [1, 9, 5, 8, 2] ) ➞ True
            EX3_5( [-6, 15, 4] ) ➞ True
        '''
    miles = 0
    if List == []:
        return False
    for number in List:
        if number < 0:
            number = -number
        miles += number
    if miles == 25:
        return True
    else:
        return False
