def EX3_2(List):
    '''
    (list) -> int
        
        This is the "Max Adjacent Product" function. 
        Given a list of integers, this function finds the pair of adjacent
        elements that have the largest product and 
        return that product.
        
        NOTE: Each list has at least two elements.
        
        Examples:
        
            EX3_2( [3, 6, -2, -5, 7, 3] ) ➞ 21
            EX3_2( [5, 6, -4, 2, 3, 2, -23] ) ➞ 30
            EX3_2( [0, -1, 1, 24, 1, -4, 8, 10] ) ➞ 80
        '''
    x = 0
    y = 0
    for number in List:
        if number >= x:
            x = number
        if y <= number < x:
            y = number
    print( x*y)
