def EX3_4(x,y,z):
    '''
    (int | float , int | float , int | float) -> bool
    
        This is the "Multi Division" function.
        For a given x,y,z adds the number x to itself y times
        and checks if it is devisable by z.
        
        Examples:
        
            EX3_4(42, 5, 10) ➞ False
                # 42+42 = 84,84+84 = 168,168+168 = 336,336+336 = 672, 672+672 = 1344
                # 1344 is not divisible by 10
                
                EX3_4(5, 2, 1) ➞ True
                EX3_4(1, 2, 3) ➞ False
        '''
    n = x * 2**y
    if n%z == 0:
        return True
    else:
        return False
