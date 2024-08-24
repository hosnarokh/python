player_count = int(input())
player_game_count = [i for i in map(int, input().split()) if i < 3]

print(len(player_game_count) // 3)
