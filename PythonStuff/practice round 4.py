from itertools import permutations
from collections import Counter
from ssl import Options


def complaints(scores, test, friends):
    score = 0
    for i in range(len(test)):
        if test[i] == '1':
            score += scores[i]
        else:
            score += friends - scores[i]
    return score


def solve():
    M = list(map(int, input().split())) # friends, exceptions, options
    orders = []
    bad = []
    for i in range(M[0]):
        orders.append(str(input()))
    
    for i in range(M[1]):
        bad.append(str(input()))
    
    scores = [0]*M[2] # [2, 1, 1, 0]

    for i in range(len(orders)):
        for j in range(M[2]):
            if orders[i][j] == '1':
                scores[j] += 1

    attempt = ''
    for i in range(M[2]):
        attempt += '0'


    # mmake a binary tree to test all possibilities

    test = ''

    for i in range(M[2]):
        for j in range(2):

        poo = complaints(scores, test, M[0])
        if test not in bad:
            return poo

    




if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(f'Case #{i+1}: {solve()}')



