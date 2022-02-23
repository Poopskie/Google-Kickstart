from itertools import permutations
from collections import Counter


def solve():
    S = input()
    letters = []
    ans = ''

    for letter in S:
        letters.append(letter)

    perms = list(permutations(letters))

    for i in range(len(perms)):
        temp = perms[i]
        word = ''
        for j in range(len(temp)):
            if temp[j] != S[j]:
                word += temp[j]
                continue
            else:
                break
        else:
            return word
    
    return 'IMPOSSIBLE'
        


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(f'Case #{i+1}: {solve()}')



