
import random
def print_pencils():
    print("|" * total_pencils)

def player_switcher(current_player):
    if current_player == players[0]:
        return players[1]
    else:
        return players[0]

def bot_move(total_pencils):
    if total_pencils == 1:
        return 1
    elif total_pencils % 4 == 1:
        return 1
    else:
        if total_pencils % 4 == 0:
            return 3
        elif total_pencils % 4 == 3:
            return 2
        else:
            return 1

total_pencils = input("How many pencils would you like to use: ")
while not total_pencils.isdigit() or int(total_pencils) <= 0:
    if not total_pencils.isdigit():
        print("The number of pencils should be numeric")
    else:
        print("The number of pencils should be positive")
    total_pencils = input()

total_pencils = int(total_pencils)

first_turn = input("Who will be the first (John, Jack): ")
players = ["Jack", "John"]
while not first_turn in players:
    print("Choose between 'John' and 'Jack'")
    first_turn = input()
players = ["Jack", "John"] if first_turn == "Jack" else ["John", "Jack"]
current_player = players[0]

while total_pencils > 0:
    print_pencils()
    if current_player == "Jack":
        bot_move_value = bot_move(total_pencils)
        print(current_player + "'s turn!\n", bot_move_value)
        total_pencils -= bot_move_value
    else:
        print(current_player + "'s turn!")
        players_pencils = input()
        while not players_pencils.isdigit() or int(players_pencils) not in (1, 2, 3):
            print("Possible values: '1', '2' or '3'")
            players_pencils = input()
        players_pencils = int(players_pencils)
        while players_pencils > total_pencils or players_pencils > 3:
            print("Too many pencils were taken")
            players_pencils = int(input())
        total_pencils -= players_pencils
    current_player = player_switcher(current_player)
    if total_pencils == 0:
        break


print(current_player + " won!")
