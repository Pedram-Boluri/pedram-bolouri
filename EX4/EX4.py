def EX4():
    '''
    None -> None

    Given the coordination of knight and bishop ona chess boeard as a letter and number,
    this function will tell you, if possible, which one will attack the other.

    Note: If any of the given variables are not in the standard form,
    the function will show an error and stop working untill called again.
    '''
    # validation
    invalid_list = ['!','@','#','$','%','^','^','&','*','-','_','+','=',',','.','*','/','?','']
    while True:
        Knight_horizantal_position = input(('Please enter {} position of {} {}: ').format('horizontal','knight','(a,b,c,d,e,f,g,h)'))
        if Knight_horizantal_position not in ['a','b','c','d','e','f','g','h','A','B','C','D','E','F','G','H']:
            if len(Knight_horizantal_position)>1:
                print ('Horizontal input for knight is not a letter')
                break
            elif Knight_horizantal_position not in 'abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print('Horizontal input for knight is not a letter')
                break
            else:
                print('Horizontal input for knight is not a proper letter')
                break
        Knight_vertical_position = (input(('Please enter {} position of {} {}:  ').format('vertical','knight','(1,2,3,4,5,6,,7,8)')))
        if Knight_vertical_position not in ('0','1','2','3','4','5','6','7','8'):
            if ((Knight_vertical_position)<='0') and (Knight_vertical_position in invalid_list):
                print('Vertical input for knight is not a number')
                break
            elif Knight_vertical_position in 'abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print('Vertical input for knight is not a number')
                break
            elif ((Knight_vertical_position)>'0'):
                print('Vertical input for knight is not a propper number')
                break
        Bishop_horizontal_position = input(('Please enter {} position of {} {}: ').format('horizontal','bishop','(a,b,c,d,e,f,g,h)'))
        if Bishop_horizontal_position not in ['a','b','c','d','e','f','g','h','A','B','C','D','E','F','G','H']:
            if len(Bishop_horizontal_position)>1:
                print ('Horizontal input for bishop is not a letter')
                break
            elif Bishop_horizontal_position not in 'abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print('Horizontal input for bishop is not a letter')
                break
            else:
                print('Horizontal input for bishop is not a proper letter')
                break
        Bishop_vertical_position = (input(('Please enter {} position of {} {}:  ').format('vertical','bishop','(1,2,3,4,5,6,,7,8)')))
        if Bishop_vertical_position not in ('0','1','2','3','4','5','6','7','8'):
            if ((Bishop_vertical_position)<='0') and (Bishop_vertical_position in invalid_list):
                print('Vertical inputfor bishop  is not a number')
                break
            elif Bishop_vertical_position in 'abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print('Vertical input for bishop is not a number')
                break
            elif ((Bishop_vertical_position)>'0'):
                print('Vertical input for bishop for bishop is not a propper number')
                break
        if (Knight_horizantal_position == Bishop_horizontal_position) and (Knight_vertical_position == Bishop_vertical_position):
            print("They can't be in the same square")
            break
    #===========================================================================================================================
    # Changing horizontal values to int
    # This part should be changed into a Dictionary. 
        Knight_vertical_position = int(Knight_vertical_position)
        Bishop_vertical_position = int(Bishop_vertical_position)
        letter_list = ['a','b','c','d','e','f','g','h']
        LETTER_LIST = ['A','B','C','D','E','F','G','H']
        number_list = [11,22,33,44,55,66,77,88]
        if Knight_horizantal_position in letter_list:
            ii = letter_list.index(Knight_horizantal_position)
            Knight_horizantal_position = number_list[ii]
        if Knight_horizantal_position in LETTER_LIST:
            ii = LETTER_LIST.index(Knight_horizantal_position)
            Knight_horizantal_position = number_list[ii]
        if Bishop_horizontal_position in letter_list:
            ii = letter_list.index(Bishop_horizontal_position)
            Bishop_horizontal_position = number_list[ii]
        if Bishop_horizontal_position in LETTER_LIST:
            ii = LETTER_LIST.index(Bishop_horizontal_position)
            Bishop_horizontal_position = number_list[ii]
        # Organizing the positions
        Knight_position = [Knight_horizantal_position , Knight_vertical_position]
        Bishop_position = [Bishop_horizontal_position , Bishop_vertical_position]
        # Defining the movements:
        Knight_movement = [[11,2],[22,1],[-11,2],[-22,1],[-11,-2],[-22,-1],[11,-2],[22,-1]]
        Bishop_movement = [[11,1],[11,-1],[-11,1],[-11,-1]]
        # Knight's play
        for z in range (0,len(Knight_movement)):
            x = Knight_position[0] + Knight_movement[z][0]
            y = Knight_position[1] + Knight_movement[z][1]
            if [x,y] != Bishop_position:
                Knight_attack = False
            else:
                Knight_attack = True
                break
        # Bishop's play
        for z in range (0,len(Bishop_movement)):
            xx = Bishop_position[0]
            yy = Bishop_position[1]
            while xx <= 88 and yy <= 8:
                xx += Bishop_movement[z][0]
                yy += Bishop_movement[z][1]
                if [xx,yy] != Knight_position:
                    Bishop_attack = False
                else:
                    Bishop_attack = True
                    break
            break     
        # Finally.... Roll the drums... THE RESULTS
        if (Knight_attack == False) and (Bishop_attack == False):
            print ('Neither of them can attack each other')
            break
        elif Knight_attack == True:
            print ('Knight can attack bishop')
            break
        elif Bishop_attack == True:
            print ('Bishop can atthack knight')
            break
