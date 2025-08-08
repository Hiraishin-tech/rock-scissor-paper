import random

def game():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    options = [rock, paper, scissors]
    player_score = 0
    computer_score = 0
    number_of_rounds = 0
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'

    while True:
        try:
            player_choice = int(input("Co si vyberete? 0 pro kámen, 1 pro papír a 2 pro nůžky?\n"))
            computer_choice = random.randint(0, 2)

            print(f'Uživatel si vybral: {options[player_choice]}')
            print(f'Počítač si vybral: {options[computer_choice]}')
            if player_choice == 0:
                if computer_choice == 0:
                    print(f'{YELLOW}Je to remíza.{RESET}')
                elif computer_choice == 1:
                    print(f'{RED}Prohrál jste, počítač si vybral papír{RESET}')
                    computer_score += 1
                else:
                    print(f'{GREEN}Vyhrál jste, počítač si vybral nůžky{RESET}')
                    player_score += 1
            elif player_choice == 1:
                if computer_choice == 0:
                    print(f'{GREEN}Vyhrál jste, počítač si vybral kámen{RESET}')
                    player_score += 1
                elif computer_choice == 1:
                    print(f'{YELLOW}Je to remíza.{RESET}')
                else:
                    print(f'{RED}Prohrál jste, počítač si vybral nůžky{RESET}')
                    computer_score += 1

            else:
                if computer_choice == 0:
                    print(f'{RED}Prohrál jste, počítač si vybral kámen{RESET}')
                    computer_score += 1
                elif computer_choice == 1:
                    print(f'{GREEN}Vyhrál jste, počítač si vybral papír{RESET}')
                    player_score += 1
                else:
                    print(f'{YELLOW}Je to remíza{RESET}')

            print(f'Aktuální skóre pro hráč:počítač je {player_score}:{computer_score}')

            number_of_rounds += 1

            if number_of_rounds % 5 == 0: # After every 5 rounds there is a prompt to end the game
                endGame = input("Chcete ukončit hru? (y/n) ").lower()
                if endGame == 'y':
                    break

        except (ValueError, IndexError):
            print('Zadejte prosím validní hodnoty.')

    print(f'Finální skóre je {player_score}:{computer_score}')
    if player_score > computer_score:
        print(f'Jste finální {GREEN}vítěz{RESET} 😎')
    elif player_score == computer_score:
        print(f'Je to {YELLOW}remíza{RESET}. Snad příště vyhrajete 😉')
    else:
        print(f'{RED}Prohrál{RESET} jste proti počítači 😝')

game()