from itertools import permutations
from collections import Counter


def solve():
    S = input()
    letters = []
    ans = ''

    for letter in S:
        letters.append(letter)


    for i in range(len(S)):
        for j in range(len(S)):
            if S[i] != letters[j] and letters[j] != '_':
                ans += letters[j]
                letters[j] = '_'
                break
        else:
            print(ans)
            return 'IMPOSSIBLE'
    
    return ans


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(f'Case #{i+1}: {solve()}')



