#random to enable the computer to pick an answer
import random


user_hand = input('Enter your answer (Rock, Paper, Scissors)')
computer_answer_list = ['Rock', 'Paper', 'Scissors']
computer_hand = random.choice(computer_answer_list)

def play_game(user_hand, computer_hand):
    print(computer_hand)
    print(user_hand)


play_game(user_hand, computer_hand)

