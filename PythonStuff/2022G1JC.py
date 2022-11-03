import itertools, math # permutations
from collections import Counter # most common elements in dict
# returns dict with # of times each element occurs {('poo', 3), ('pee', 1)}

# use line = list(map(int, input().split())) for spaced integers
# list comprehension [int(i) for i in *iterable]


def solve():
    l = [int(i) for i in input().split()]
    # particpants, days, ID
    ppl = l[0]
    iD = l[2] - 1
    totals = []
    for x in range(l[1]):
        totals.append([])

    for i in range(ppl):
        line = [int(x) for x in input().split()]
        if i == iD:
            john = line.copy()
        for d in range(l[1]):
            totals[d].append(line[d])
    ans = 0

    for i in range(l[1]):
        greatest = 0
        for inner in range(ppl):
            if totals[i][inner] >greatest:
                greatest = totals[i][inner]
        if greatest > john[i]:
            ans += (greatest - john[i])
    
    return ans




if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(f'Case #{i+1}: {solve()}')



