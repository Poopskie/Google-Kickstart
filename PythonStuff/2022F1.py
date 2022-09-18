from itertools import permutations
from collections import Counter


letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
lettersl = letters.split()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
, 20, 21, 22, 23, 24, 25, 26]

alpha = {x:y for x,y in zip(lettersl, nums)}


def solve():
    t = int(input())
    lines = [] # list of all
    ordercolor = []
    orderdura = []
    for i in range(t):
        l = input().split() # [blue, 1, 2]
        lines.append(l)
    linescolor = lines.copy()
    linesdura = lines.copy()

    # color sort
    for i in range(t):
        ordercolor.append(linescolor[i][0])
    poo = sorted(ordercolor)
    for i in range(t):
        for j in range (t):
            if linescolor[j] == poo[i]:
                linescolor[j] = i


    for i in range(t):
        min_index = i
        for j in range(i+1, t):
            if linescolor[j][0] < linescolor[min_index][0]:
                min_index = j
            elif linescolor[j][0] == linescolor[min_index][0] and int(linescolor[j][2]) < int(linescolor[min_index][2]):
                min_index = j
        # i th number sorted
        linescolor[i], linescolor[min_index] = linescolor[min_index], linescolor[i]
    # dura sort
    for i in range(t):
        min_index = i
        for j in range(i+1, t):
            if int(linesdura[j][1]) < int(linesdura[min_index][1]):
                min_index = j
            elif int(linesdura[j][1]) == int(linesdura[min_index][1]) and int(linesdura[j][2]) < int(linesdura[min_index][2]):
                min_index = j
        # i th number sorted
        linesdura[i], linesdura[min_index] = linesdura[min_index], linesdura[i]
    # find matches

    ans = 0
    for i in range(t):
        if linescolor[i] == linesdura[i]:
            ans += 1
    return ans






if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(f'Case #{i+1}: {solve()}')



