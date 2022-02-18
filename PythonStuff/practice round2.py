from itertools import permutations
from collections import Counter




def solve():
    length = int(input())
    papers = list(map(int, input().split()))
    final = []
    H = 0
    for i in range(length):
        papers[i]


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(f'Case #{i+1}: ')
        print(' '.join(solve()))



