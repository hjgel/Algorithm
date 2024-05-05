# def solution(moves):
#     x = y = 0
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     move = ['U', 'R', 'D', 'L']
#     for i in moves:
#         if i in move:
#             x = x + dx[move.index(i)]
#             y = y + dy[move.index(i)]

#     return [x, y]
                            
# print(solution('RRRDDDLU'))
# print(solution('DDDRRRDDLL'))
# print(solution('RRRRRRDDDDDDUULLL'))
# print(solution('RRRRDDDRRDDLLUU'))

def solution(moves):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    move = ['U', 'R', 'D', 'L']
    for i in moves:
        for k in range(4):
            if i == move[k]:
                x = x + dx[k]
                y = y + dy[k]

        # if i in move:
        #     x = x + dx[move.index(i)]
        #     y = y + dy[move.index(i)]

    return [x, y]
                            
print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))