

def display_list(game_list):
    print("Here is the List")
    print(game_list)

def palyer_choice():

    choice = 'x'

    while choice not in ['0','1','2']:

        choice = input("Enter the position (0,1,2): ")
        if choice not in ['0','1','2']:
            print("Invalid Position! Write again!")

    return int(choice)

def replacement(game_list,position):

    replce = input("Enter the String to replace: ")

    game_list[position] = replce

    return game_list

def game_choice():

    choice = 'wrong'

    while choice not in ['Y','N']:

        choice = input("Would you like to play again?? [Y/N]: ")

        if choice not in ['Y','N']:
            print("Reply in [Y,N]")

    if choice == 'Y':
        return True
    else:
        return False    
    
    # Putting all function together

game_on = True

game_list = [0,1,2]

while game_on:

    display_list(game_list)

    choice = palyer_choice()
    
    replacement(game_list,choice)
    display_list(game_list)

    game_on = game_choice()