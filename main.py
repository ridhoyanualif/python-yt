from libs import welcome_username, panda_game, start_program, exit_program, addition_game, prize_game
def options():
    options_input = int(input("Your Options :\n1. Panda Game\n2. Addition Game\n3. Prize Game\n4. Exit\nWhich One Do You Prefer : "))
    print("")
    if options_input == 1:
        panda_game()
    elif options_input == 2:
        addition_game()
    elif options_input == 3:
        prize_game()
    elif options_input == 4:
        exit_program()
    else:
        options()
    
def main():
    start_program()
    welcome_username()
    options()

if __name__ == '__main__':
    main()