from random import choice

choices = ['rock','paper','scissors']

program = choice(choices)
player = ""

again = 'yes'

while again == 'yes':
    while player.lower() not in choices:
        player = input("rock, paper or scissors?: ")
        
    print(f"\nprogram: {program}")
    print(f"player: {player}")

    if player == program:
        print("It's a tie")
    elif player == 'rock':
        if program == 'scissors':
            print("you win")
        if program == 'paper':
            print("you loose")
    elif player == 'paper':
        if program == 'rock':
            print("you loose")
        if program == 'scissors':
            print("you win")
    elif player == 'scissors':
        if program == 'paper':
            print("you win")
        if program == 'rock':
            print("you loose")
    print()
    again = input("Wanna play again (yes/no) ?: ").lower()
    player = ""

print("The program finished")