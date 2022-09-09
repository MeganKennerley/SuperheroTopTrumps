"""Randomly generates card from deck and displays all data on screen
Randomly picks card for computer without showing data to player
Asks player with criteria they want to compare ('Intelligence', 'Strength',
'Speed', 'Durability', 'Power', 'Combat')
Compares both cards see which is the greatest number
Tells player whether they won drew or lost - the largest number
Gives the points out accordingly 3pts win, 1pts draw
Displays scores on screen and repeats until first player reaches 12pts"""

"""Pickup card from deck 
choose criteria 
compare 
win lose
put card to back"""

import random
import csv
from pprint import pprint

def load_deck():
    with open('Superheros - Filtered.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)

        deck = []

        for row in spreadsheet:
            deck.append(dict(row))

    return deck


def main():

    player_score = 0
    computer_score = 0

    while True:

        player_card = random.choice(load_deck())
        computer_card = random.choice(load_deck())

        cards = [
            {'Character Name': player_card["Character Name"]},
            {'Full Name': player_card["Full Name"]},
            {'Alter Egos': player_card["Alter Egos"]},
            {'Place Of Birth': player_card["Place Of Birth"]},
            {'Gender': player_card["Gender"]},
            {'Height': player_card["Height"]},
            {'Intelligence': player_card["Intelligence"]},
            {'Strength': player_card["Strength"]},
            {'Speed': player_card["Speed"]},
            {'Durability': player_card["Durability"]},
            {'Power': player_card["Power"]},
            {'Combat': player_card["Combat"]},
        ]

        intelligence = (player_card['Intelligence'])
        strength = (player_card['Strength'])
        speed = (player_card['Speed'])
        durability = (player_card['Durability'])
        power = (player_card['Power'])
        combat = (player_card['Combat'])


        print('This is your card: ')

        for card in cards:

            pprint(card)

        compare_card = {1: 'Intelligence', 2: 'Strength', 3: 'Speed', 4: 'Durability', 5: 'Power', 6: 'Combat'}

        player_choice = int(input('Please choose Power Stat (1. Intelligence, 2. Strength, '
                       '3. Speed, 4. Durability, 5. Power, 6. Combat): '))
        player_stat = int(player_card[compare_card[player_choice]])
        computer_stat = int(computer_card[compare_card[player_choice]])

        if player_choice == 1:
            print(intelligence)
        elif player_choice == 2:
            print(strength)
        elif player_choice == 3:
            print(speed)
        elif player_choice == 4:
            print(durability)
        elif player_choice == 5:
            print(power)
        elif player_choice == 6:
            print(combat)
        else:
            print('Choose another number.')


        if player_stat > computer_stat:
            print('You win! You get 3 points!')
            print(f'Your stat: {player_stat} \nOpponent\'s stat: {computer_stat}')
            player_score += 3
        elif player_stat == computer_stat:
            print('It\'s a draw! You get 1 point.')
            player_score += 1
            computer_score += 1
        else:
            print('You lost!')
            print(f'Your stat: {player_stat} \nOpponent\'s stat: {computer_stat}')
            computer_score += 3

        print(f'Your score is: {player_score} \nComputer score is: {computer_score}')

        if player_score >= 12 or computer_score >= 12:
            print(f'Game Over!')
            break


main()






