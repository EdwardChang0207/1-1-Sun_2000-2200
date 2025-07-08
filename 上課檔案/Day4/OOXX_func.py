def place_player(game_map, player):
    x, y = map(int, input().split())
    game_map[x][y] = player
    print(*game_map, sep='\n')
    return game_map

def count_amount(l:list,player):
    if l.count(player) == 3:
        print(f'{player} Win!')
        return False
    return True
def judge(game_map, player):
    for row in game_map:
        game = count_amount(row)
    for i in range(len(game_map[0])):
        col = []
        for j in range(len(game_map)):
            col.append(game_map[j][i])
        if col.count(player) == 3: #直
            print(f'{player} Win!')
            return False
    if [game_map[0][0], game_map[1][1], game_map[2][2]].count(player) == 3:
        print(f'{player} Win!')
        return False
    if [game_map[0][2], game_map[1][1], game_map[2][0]].count(player) == 3:
        print(f'{player} Win!')
        return False


game_map = [
    ['','',''],#0
    ['','',''],#1
    ['','','']#2
    # 0  1  2
]
game = True
player = 'O'
while game:
    game_map = place_player(game_map, player)
    game = judge(game_map, player)