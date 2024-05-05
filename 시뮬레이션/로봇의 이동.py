def solution(moves):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    d = 1
    
    for c in moves:
        if c == 'G':
            x = x + dx[d]
            y = y + dy[d]
        elif c == "R":
            d = (d + 1) % 4 
        
        else:
            d -= 1

    return [x, y]
                      
print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))
