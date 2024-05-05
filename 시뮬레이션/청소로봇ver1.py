def solution(moves):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in moves:
        if i == 'U':
            x = x + dx[0]
            y = y + dy[0]
        elif i == 'R':
            x = x + dx[1]
            y = y + dy[1]
        elif i == 'D':
            x = x + dx[2]
            y = y + dy[2]
        elif i == 'L':
            x = x + dx[3]
            y = y + dy[3]

    return [x, y]
                            
print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))
