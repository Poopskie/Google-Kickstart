from itertools import permutations
from collections import Counter


# fuck fuck fuck, man ok so
# the problem is cause im moving up/down on a square thats the wrong colour, not on one that works



def solve():
    N = int(input())
    board = [] # bunch of strings
    blue = 0
    red = 0
    blue_win_index = set()
    red_win_index = set()
    displacement = 0
    

    for i in range(N):
        board.append(input())
        for j in range(N):
            if board[i][j] == 'B':
                blue += 1
            elif board[i][j] == 'R':
                red += 1    

    i = 0
    while i < N:
        j = 0
        while j < N:
            check = board[i][j]
            if check != 'B':
                try:
                    if board[i+1][j] == 'B':
                        i += 1
                        continue
                    elif board[i-1][j] == 'B':
                        i -= 1
                        continue
                    elif board[i+1][j-1] == 'B':
                        i += 1
                        j -= 1
                        continue
                    elif board[i-1][j+1] == 'B':
                        i -= 1
                        j += 1
                        continue
                    else:
                        break
                except:
                    break
            j += 1

        else:
            if (i, j) not in blue_win_index:
                blue_win_index.add((i, j))
            else:
                displacement += 1
                i += displacement
        i += 1
    
    displacement = 0
    i = 0
    while i < N:
        j = 0
        while j < N:
            check = board[j][i]
            if check != 'R':
                try:
                    if board[j][i+1] == 'R':
                        i += 1
                        continue
                    elif board[j][i-1] == 'R':
                        i -= 1
                        continue
                    elif board[j+1][i-1] == 'R':
                        i -= 1
                        j += 1
                        continue
                    elif board[j-1][i+1] == 'R':
                        i += 1
                        j -= 1
                        continue
                    else:
                        break
                except:
                    break
            j += 1
        else:
            if (i, j) not in red_win_index:
                red_win_index.add((i, j))
            else:
                displacement += 1
                i += displacement
        i += 1
    
    if abs(blue - red) >= 2:
        return 'Impossible'
    elif len(blue_win_index) + len(red_win_index) == 0:
        return 'Nobody wins'
    elif len(blue_win_index) == 1:
        return 'Blue wins'
    elif len(red_win_index) == 1:
        return 'Red wins'
    else:
        return 'Impossible'
    
    



if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(f'Case #{i+1}: {solve()}')



