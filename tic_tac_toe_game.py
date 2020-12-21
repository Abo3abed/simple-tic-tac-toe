from random import randint
from ascii_art import user_1_wins, user_2_wins


def flip_player(player_number: int) -> int:
    if player_number == 1:
        return 2
    else:
        return 1


player = randint(1, 2)
players = {
    1: ['X', []],
    2: ['O', []]
}
winner = 1
inputs = []
win_cases = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
is_going = True

with open('panel.txt') as panel:
    data = panel.read()
    print(data)
    print(f'user {player} should play first!')
    while is_going:
        for _ in range(1, 100):
            player_input = int(input(f'user {player} choose a number as displayed: '))
            if player_input not in inputs and player_input in range(1, 10):
                inputs.append(player_input)
                players[player][1].append(player_input)
                break
            else:
                print(f'Sorry! choose only the numbers displayed above!')
        data = data.replace(f'[{player_input}]', players[player][0])
        players[player][1].sort()
        if players[player][1] in win_cases:
            winner = player
            is_going = False
        player = flip_player(player_number=player)
        print(data)
    print(user_1_wins if winner == 1 else user_2_wins)
