from itertools import permutations
from collections import Counter




def solve():
    length = int(input())
    papers = list(map(int, input().split()))
    final = []
    greatest_list = []
    H = 0
    for i in range(length):
        if papers[i] > H:
            greatest_list.append(papers[i])
        H = len(greatest_list)
        for num in greatest_list:
            if num < H:
                greatest_list.remove(num)
        H = len(greatest_list)
        final.append(H)
    return final


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(f'Case #{i+1}:', end=' ')
        print(' '.join(list(map(str, solve()))))



