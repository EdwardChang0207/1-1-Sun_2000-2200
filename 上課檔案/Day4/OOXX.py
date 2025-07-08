'''
game_map = [['' for j in range(3)] for i in range(3)]
'''

game_map = [
    ['','',''],#0
    ['','',''],#1
    ['','','']#2
    # 0  1  2
]
game = True
player = 'O'
while game:
    x, y = map(int, input().split())
    game_map[x][y] = player
    print(*game_map, sep='\n')
    for row in game_map:
        if row.count(player) == 3: #橫
            print(f'{player} Win!')
            game = False
            break
    for i in range(len(game_map[0])):
        col = []
        for j in range(len(game_map)):
            col.append(game_map[j][i])
        if col.count(player) == 3: #直
            print(f'{player} Win!')
            game = False
            break
    if [game_map[0][0], game_map[1][1], game_map[2][2]].count(player) == 3:
        print(f'{player} Win!')
        game = False
        break
    if [game_map[0][2], game_map[1][1], game_map[2][0]].count(player) == 3:
        print(f'{player} Win!')
        game = False
        break

    if player == 'O': player = 'X'
    else: player = 'O'