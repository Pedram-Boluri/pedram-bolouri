def EX1_5 (number):
    '''
 (int)-> str

 This funnction will tell you if the person whom age is given is an infant,
 child,teenager or an adult.
 '''
 
    if number < 1:
        print ('Infant')
    elif 1 < number < 13:
        print ('Child')
    elif 13 <= number < 20:
        print ('Teenager')
    elif number >= 20:
        print('Adult')
    return EX1_5

