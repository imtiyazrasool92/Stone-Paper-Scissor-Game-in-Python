import random
from random import randint

myList = ["stone","paper","scissor"]

cpu_score = 0
player_score =0
total_play = 0

def help():
    print("""   
    ---Help---   
    Enter s to Start the game and use
    Stone, paper and scissor as input to play
    ----------
        """)


def start():
    print("Game Started : : Enter Input ")
    global cpu_score , player_score , total_play
    while total_play != 3:
        player_input = input("> ")
        if player_input.lower() not in myList:
            print("Error Try Again !")
            continue
        cpu_input = random.choice(myList)
        player_input = player_input.lower()

        if player_input == cpu_input:
            print(f"""
            Your Choice : {player_input}
            Cpu Choice : {cpu_input}
            Draw!

            Your score : {player_score}
            Cpu score : {cpu_score}
            """)
        elif player_input == "stone" and cpu_input == "paper":
            cpu_score += 1
            print(f"""
            Your Choice : {player_input}
            Cpu Choice : {cpu_input}

            Your score : {player_score}
            Cpu score : {cpu_score}
            """)
        elif player_input == "stone" and cpu_input == "scissor":
            player_score += 1
            print(f"""
            Your Choice : {player_input}
            Cpu Choice : {cpu_input}

            Your score : {player_score}
            Cpu score : {cpu_score}
            """)
        elif player_input == "paper" and cpu_input == "stone":
            player_score += 1
            print(f"""
            Your Choice : {player_input}
            Cpu Choice : {cpu_input}

            Your score : {player_score}
            Cpu score : {cpu_score}
            """)
        elif player_input == "paper" and cpu_input == "scissor":
            cpu_score += 1
            print(f"""
            Your Choice : {player_input}
            Cpu Choice : {cpu_input}

            Your score : {player_score}
            Cpu score : {cpu_score}
            """)
        elif player_input == "scissor" and cpu_input == "paper":
            player_score += 1
            print(f"""
            Your Choice : {player_input}
            Cpu Choice : {cpu_input}

            Your score : {player_score}
            Cpu score : {cpu_score}
            """)
        elif player_input == "scissor" and cpu_input == "stone":
            cpu_score += 1
            print(f"""
            Your Choice : {player_input}
            Cpu Choice : {cpu_input}

            Your score : {player_score}
            Cpu score : {cpu_score}
            """)
        total_play += 1

def winner():
    global player_score , cpu_score
    if player_score > cpu_score:
        print(f"""
        You Won !
        Your Score: {player_score}
        CPU Score : {cpu_score}
        """)

while True:
    print("""
    To start enter (s)
    For Help enter (h)
    To exit enter (e)
    """)
    user_input = input("> ")
    if user_input == 's':
        start()
        winner()
        break
    elif user_input == 'h':
        help()
    elif user_input == 'e':
        break
print("Thanku For Playing")