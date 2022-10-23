def EX1_6(number):
    '''

 (int)-> str



 Tis function will give you the roman version of the number you give.

   Notice: This function only works with numbers between 1 and 10

   '''
    if number == 1:
        x = ("I")
    elif number == 2:
        x =("II")
    elif number == 3:
        x = ("III")
    elif number == 4:
        x = ("IV")
    elif number == 5:
        x = ("V")
    elif number == 6:
        x = ("VI")
    elif number == 7:
        x = ("VII")
    elif number == 8:
        x = ("VIII")
    elif number == 9:
        x = ("IX")
    elif number == 10:
        x = ("X")
    elif number > 10:
        x = ("Error")
    print (x)
    return EX1_6
