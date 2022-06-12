# Zuri_Task Rock-Paper-Scissors
#Olalekan  Asaaju____ZuriID:_I4G013117BWF_Metro @Zuri Training 2022

import random

CHOICES = ['r', 'p', 's' ]
 
def Rock_Paper_Scissors():
    def get_player_choice():
#Get user input and validate it
        player_choice = None
        while player_choice is None:
            player_choice = input('AVAILABLE OPTIONS: R, P, and S \n"R" for "Rock" \n"P" for "Paper" \n"S" for "Scissors" \n\nChoose an optons : ')
            if player_choice.lower() not in CHOICES: 
                print( "\nInvalid option, option must be R, P or S\n")
                return get_player_choice()
            else:
                return player_choice.lower()

    
    def get_computer_choice():
        #Have the computer pick one of the valid choices at random
        CPU = random.randint(0, 2)
        CPU  = CHOICES[CPU ]
        return CPU
    
  
    def draw_game(player_choice, CPU ):
        #Check if game was a draw
        if player_choice == CPU :
            return True
            

    def print_winner(player_choice, CPU ):
        #Check to see who won
        if player_choice == 'r' and CPU  == 's':
            print('Player wins!')
        elif player_choice == 's' and CPU  == 'p':
            print('Player wins!')
        elif player_choice == 'p' and CPU  == 'r':
            print('Player wins!')
        else:
            print('CPU  wins!')
            print('%s beats %s' % (CPU , player_choice))
        print("Game over!")

    for x in range (3): 
        def play_game():
        #Game controller 
            player_choice = get_player_choice()
            CPU  = get_computer_choice()
            if draw_game(player_choice, CPU ):
                print("It's a draw, both players picked %s: \n\n" % player_choice)
                return Rock_Paper_Scissors()
            else:
                print("CPU  picked: %s" % CPU )
                print("Player picked: %s" % player_choice)
                print_winner(player_choice, CPU )
                #return Rock_Paper_Scissors()
            
                    

    if __name__ == "__main__":
        play_game()

if __name__ == "__main__":
    Rock_Paper_Scissors()


        
