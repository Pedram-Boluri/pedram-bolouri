def EX3_3 (List):
    '''
    (List) -> bool

        This is the "Robot Path" function, which works by giving it a set
        of movement commands. The commands are 'n,' 'e,' 's,' and 'w'(North,
        East, South and West). The robot moves one step for each command in
        the respective direction.
        
        The function will returns True if the robot reaches any of the wanted 
        destinations, False otherwise.

        The acceptable destinations are:
            Destination No. 1: e, n, e, e, n
            Destination No. 2: w, n, w, n, w, w, n
            
        Examples:
            EX3_3( ["s", "e", "e", "n", "n", "e", ”n"] ) ➞ True
            # Robot will end up at destination no. 1
            
            EX3_3( ["n", "e", "s", "w", "n", "e", "s", "w", "w", \
            "s", "n", ”e"] ) ➞ False
            # Robot will be lost somewhere
            
            EX3_3( ["n", "s", "n", "n", "e", "n", "w", \
            "w", "s", "w", "w", "w", ”n"] ) ➞ True
        '''


    x = 0
    y = 0 
    for direction in List:
        if direction == 'n':
            x += 1
        elif direction == 's':
            x -= 1
        elif direction == 'e':
            y += 1
        elif direction == 'w':
            y -= 1
            
    if (x == 2 and y == 3) or (x == 3 and y == -4):
        return True 
    else:
        return False
