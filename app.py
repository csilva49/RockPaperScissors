#random to enable the computer to pick an answer
import random


#initial variables
user_hand = ""
computer_answer_list = ['Rock', 'Paper', 'Scissors']
score = 0

#check if user ended the game
while user_hand != 'd':
    user_hand = input('Enter your answer (a) Rock,(b) Paper,(c) Scissors,(d) End Game  : ')
    computer_hand = random.choice(computer_answer_list)
    #test answer
    if user_hand == 'a' or user_hand == 'b' or user_hand == 'c':
        #if computer picks rock
        if computer_hand == 'Rock':
            if user_hand == 'a':
                print('The computer picked Rock, it\'s a draw!\n\n Your score is  ' + str(score))
            elif user_hand == 'b':
                #if user wins, add 1 point to board
                score += 1
                print('The computer picked Rock, you win!\n\n Your score is  ' + str(score))
            else:
                #if user loses, substract 1 point to board, if score is 0 dont do anything
                if score > 0:
                    score -= 1

                print('The computer picked Rock, you lost!\n\n Your score is  ' + str(score))

        #if computer picks paper
        if computer_hand == 'Paper':
            if user_hand == 'a':
                #if user loses, substract 1 point to board, if score is 0 dont do anything
                if score > 0:
                    score -= 1
                print('The computer picked Paper, you lost!\n\n Your score is  ' + str(score))
            elif user_hand == 'b':
                print('The computer picked Paper, it\'s a draw!\n\n Your score is  ' + str(score))
            else:
                #if user wins, add 1 point to board
                score += 1
                print('The computer picked Paper, you win!\n\n Your score is  ' + str(score))

        #if computer picks scissors
        if computer_hand == 'Scissors':
            if user_hand == 'a':
                #if user wins, add 1 point to board
                score += 1
                print('The computer picked Scissors, you win!\n\n Your score is  ' + str(score))
            elif user_hand == 'b':
                #if user loses, substract 1 point to board, if score is 0 dont do anything
                if score > 0:
                    score -= 1
                print('The computer picked Scissors, you lost!\n\n Your score is  ' + str(score))
            else:
                print('The computer picked Scissors, it\'s a draw!\n\n Your score is  ' + str(score))
    else:
        print('You choose an impossible hand, please restart the game...')
else:
    print('You have ended the game! Your final score is '+ str(score))
    


