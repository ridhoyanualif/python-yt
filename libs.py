def welcome_python():
    print("**************")
    print("*** WELCOME **")
    print("***** TO *****")
    print("*** PYTHON ***")
    print("**************")


def welcome_message(title):
    style = "*" * (len(title) + 4)
    print(style)
    print(f"  {title}  ")
    print(style)
    print("")


def welcome_username():
    import socket
    pc_name = socket.gethostname()
    style = "*" * (len(pc_name) + 4)
    print(style)
    print(f"  {pc_name}  ")
    print(style)
    print("")


def addition_game():
    from main import options
    
    input_name = input("Your Name : ")
    print(f'''Hi {input_name}! Choose Two Number From :
    1   2   3   4   5   6   7   8   9   10     
    ''')
    
    input_choise = int(input("Your Choise = "))
    input_choise2 = int(input("Choose One More Number = "))
    print(f"Ok, We Have {input_choise} and {input_choise2}")
    
    program_result = input_choise + input_choise2
    user_result = int(input(f"How Much {input_choise} + {input_choise2} = "))
    
    if user_result == program_result:
        print("Right Answer!")
    else:
        print("Try Again!")
        
    print("")
    try_input = input("Try Again? (y/n) = ")
    print("")

    while try_input == "":
        try_input = input("Try Again? (y/n) = ")
        print("")

    if try_input == "n":
        options()
    elif try_input == "y":
        addition_game()
        
    if __name__ == '__main__': 
        addition_game()
    
def exit_program():
    from time import sleep
    print("  -->  |")
    sleep(1)
    print("   --> |")
    sleep(1)
    print("    -->|")
    sleep(1)
    print("       |Bye")


def start_program():
    from time import sleep
    print("  -->  |")
    sleep(1)
    print("   --> |")
    sleep(1)
    print("    -->|")
    sleep(1)
    print("       |Hi!")
    print("")

    
def panda_game():
    from main import options
    import random

    panda_position = random.randint(1, 6)

    door = " [_] "
    interface = [door] * 6
    visible_interface = interface.copy()
    visible_interface[panda_position - 1] = " [0_0] "
    interface = ' '.join(interface)
    visible_interface = ' '.join(visible_interface)
    print(interface)
    
    user_pick = int(input("Guess Door That Panda Hiding {1, 2, 3, 4, 5, 6} = "))
    
    if user_pick == panda_position:
        print(f"You Guess It Right! {visible_interface}")
    else:
        print(f"Wrong Guess! The Panda Hiding In {visible_interface}")
        
    print("")
    try_input = input("Try Again? (y/n) = ")
    print("")

    while try_input == "":
        try_input = input("Try Again? (y/n) = ")
        print("")

    if try_input == "n":
        options()
    elif try_input == "y":
        panda_game()
        
    if __name__ == '__main__': 
        panda_game()
        
    
def prize_game():
    from main import options
    
    car = ["ferrari", "honda", "toyota", "mercedes", "skoda", "volvo", "suzuki", "alfa romeo", "lamborghini", "Nissan"]
    print(f"We Have Car Array That Contains {len(car)} Data")
    user_input = int(input("Choose Your Number From 1 - 10 = "))
    if user_input > 10:
        print("Unknown Choice! Try Again")
    elif user_input < 1:
        print("Unknown Choice! Try Again")
    else:
        prize = (car[user_input - 1])
        print(f"You Got A {prize}")
        
    print("")
    try_input = input("Try Again? (y/n) = ")
    print("")

    while try_input == "":
        try_input = input("Try Again? (y/n) = ")
        print("")

    if try_input == "n":
        options()
    elif try_input == "y":
        prize_game()
        
    if __name__ == '__main__': 
        prize_game()