import sys
import random
from functools import partial

# funtion to check input from user is of the correct type
# check type int here; 

def check_input(question):
    """Funtion to check input from user is of the correct type.
    
    Parameters
    ----------
    question : string
    
    Returns
    -------
    user_input
    """
    
    user_input = input(question)
    print(f'enteries --{user_input}-- are acceptable.')
    return user_input

#q_words = partial(check_input, question)
            
# function to print introduction to the game

def print_info(): 
    
    """Prints the categories of the game to screen."""
    print('''the categories:\n
    M\tA\tS\tH\n
        [1]\tResidence
        [2]\tPartner
        [3]\tNumber of kids
        [4]\tCar
        ''')
        
# function to determine type of residence

def get_residence():
    #"""Function to determine type of residence."""

    while True:
        q_residence = input('type the letter "r" to begin playing MASH.\t')
        q_rules = input('did you follow directions? \'y\' to continue...')

        if q_rules == 'r' or 'R':
            q_residence = ['mansion', 'apartment', 'shack', 'house']
            out = random.choice(q_residence)
            
            print('you will live in a: ' + (out))
            return out
            
# function to determine partner name

def get_partner():
    """Function to determine partner name."""
    
    while True:
        q_partners = input('please enter 4 first names. Separate these names using the spacebar.\t')
        q_rules = input('did you follow directions? \'y\' to continue...')

        if q_rules != 'n':
            partners_list = q_partners.split(' ')
            out = random.choice(partners_list)

            print('your partner is: ' + (out))
            return out
        
# function to determine number of kids

def get_kids():
    """Function to determine number of kids."""
    
    while True:
        q_kids = input('please enter 4 numbers (type the numbers out in words) of how many children you would like to have. Separate these numbers using the spacebar.\n\texample -- one two three four\t')
        q_rules = input('did you follow directions? \'y\' to continue...')
        
        if type(q_rules) != 'n':
            kids_list = q_kids.split(' ')
            out = random.choice(kids_list)
            
            print('you will have ' + (out) + ' kids')
            return out
            
# function to determine type of car

def get_car():
    """Function to determine type of car."""
    
    while True:
        q_cars = input('please enter 4 types of cars you would like to have. Separate these cars using the spacebar.\t')
        q_rules = input('did you follow directions? \'y\' to continue...')
        
        if q_rules != 'n':
            cars_list = q_cars.split(' ')
            out = random.choice(cars_list)
            
            print('you will drive a: ' + (out))
            return out
