#random to enable the computer to pick an answer
import random

#initial variables
user_hand = input('Enter your answer (a) Rock,(b) Paper,(c) Scissors) : ')
computer_answer_list = ['Rock', 'Paper', 'Scissors']
computer_hand = random.choice(computer_answer_list)

def play_game(user_hand, computer_hand):
    #test answer
    if user_hand == 'a' or user_hand == 'b' or user_hand == 'c':
        #if computer picks rock
        if computer_hand == 'Rock':
            if user_hand == 'a':
                return print('The computer picked Rock, it\'s a draw!')
            elif user_hand == 'b':
                return print('The computer picked Rock, you win!')
            else:
                return print('The computer picked Rock, you lost!')

        #if computer picks paper
        if computer_hand == 'Paper':
            if user_hand == 'a':
                return print('The computer picked Paper, you lost!')
            elif user_hand == 'b':
                return print('The computer picked Paper, it\'s a draw!')
            else:
                return print('The computer picked Paper, you win!')
    
        #if computer picks scissors
        if computer_hand == 'Scissors':
            if user_hand == 'a':
                return print('The computer picked Scissors, you win!')
            elif user_hand == 'b':
                return print('The computer picked Scissors, you lost!')
            else:
                return print('The computer picked Scissors, it\'s a draw!')
    else:
        print('You choose an impossible hand, please restart the game...')
    

#start the game
play_game(user_hand, computer_hand)

