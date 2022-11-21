def EX3_6(List):
    '''
    (list) -> str
        
        This is the "Face Interval" function. 
        This function takes a list and returns ":)" if the interval of the list is equal to any other 
        element; otherwise return “:(". 
        NOTE: If the given list is empty, the function will return ":/".
        
        Examples:
        
            EX3_6( [1, 2, 5, 8, 3, 9] ) ➞ ":)"
                # List interval is 8 and equal to one of the other elements.
                
            EX3_6( [5, 2, 8, 3, 11] ) ➞ ":("
                # List interval is 9 and not among the other elements.
                
            EX3_6( [ ] ) ➞ ":/"
                #[] is empty list.
'''
    if List == []:
        return ':/'
    else:
        interval = List[-1] - List[0]
        if interval in List:
            return ':)'
        else: 
            return ':('
