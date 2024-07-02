import random
import time

OPTIONS = ["rock", "paper", "scissors"]

def player_option():
    for i in range(len(co_list)):
        if player_choice.lower() == "rock":
            if co_list[i] == "rock":
                print("It is a tie!")
                points[0] += 1
                points[i+1] += 1
            if co_list[i] == "paper":
                print("It is a lost!")
                if points[0] > 0:
                    points[0] -= 1
                points[i+1] += 1
            if co_list[i] == "scissors":
                print("It is a win!")
                points[0] += 1
        elif player_choice.lower() == "paper":
            if co_list[i] == "paper":
                print("It is a tie!")
                points[0] += 1
                points[i+1] += 1
            if co_list[i] == "scissors":
                print("It is a lost!")
                if points[0] > 0:
                    points[0] -= 1
                points[i+1] += 1
            if co_list[i] == "rock":
                print("It is a win!")
                points[0] += 1
        elif player_choice.lower() == "scissors":
            if co_list[i] == "scissors":
                print("It is a tie!")
                points[0] += 1
                points[i+1] += 1
            if co_list[i] == "rock":
                print("It is a lost!")
                if points[0] > 0:
                    points[0] -= 1
                points[i+1] += 1
            if co_list[i] == "paper":
                print("It is a win!")
                points[0] += 1

def co_option():
    co_list.clear()
    for _ in range(((len(points))-1)):
        co_choice = random.choice(OPTIONS)
        co_list.append(co_choice)

while True:
    try:
        player_count = int(input("How many players would be play the game? "))
        score = int(input("What will be the max score? "))
        if player_count and score > 0:
            print("You are Player 1, good luck!")
            break
        else:
            print("Invalid option! Try again.\n")
            continue
    except:
        print("Invalid option! Try again.\n")
        continue

points = [0 for _ in range(player_count)]
co_list = []

while max(points) < score:
    player_choice = input(f"\n{ {'Player '+ str(i+1): point for i, point in enumerate(points)}}\nChoose one of the options to continue; ROCK, PAPER, or SCISSORS. [E] for exit the game. ")
    if player_choice.lower() != "e" and player_choice.lower() in OPTIONS:
        time.sleep(1)
        co_option()
        player_option()
    elif player_choice.lower() == "e":
        print(f"\n{ {'Player '+ str(i+1): point for i, point in enumerate(points)}}\nWinner is Player {points.index(max(points)) +1}!\n")
        break
    else:
        print("Invalid option! Try again.")
else:
    print(f"\n{ {'Player '+ str(i+1): point for i, point in enumerate(points)}}\nWinner is Player {points.index(max(points)) +1}!\n")