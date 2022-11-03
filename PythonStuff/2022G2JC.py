import itertools, math # permutations
from collections import Counter # most common elements in dict
# returns dict with # of times each element occurs {('poo', 3), ('pee', 1)}

# use line = list(map(int, input().split())) for spaced integers
# list comprehension [int(i) for i in *iterable]


def solve():
    radius = [int(i) for i in input().split()]
    rstone = radius[0]
    rhouse = radius[1]
    N = int(input())
    red_dist = []
    yel_dist = []
    for i in range(N):
        line = list(map(int, input().split()))
        red_dist.append(math.sqrt((line[0]**2)+(line[1]**2)))
    red_dist.sort()


    M = int(input())

    if M != 0:
        for i in range(M):
            line = list(map(int, input().split()))
            yel_dist.append(math.sqrt((line[0]**2)+(line[1]**2)))

        
        yel_dist.sort()

    ans = [0,0]

    rindex = 0
    yindex = 0

    for i in range(N+M):
        if yel_dist == []:
                if red_dist[rindex] > (rstone+rhouse):
                    break
                ans[0] += 1
                rindex += 1
        elif red_dist == []:
            if yel_dist[yindex] > (rstone+rhouse):
                break
            ans[1] += 1
            yindex += 1
    
    if ans[0] > 0 or ans[1] > 0:
        return f'{ans[0]} {ans[1]}'


    rindex = 0
    yindex = 0

    for i in range(N+M):
        try:
            if rindex > 0 and yindex > 0:
                break
            elif red_dist[rindex] > (rstone+rhouse) and yel_dist[yindex] > (rstone+rhouse): 
                break
            if red_dist[rindex] < yel_dist[yindex]:
                rindex += 1
                if rindex > 0 and yindex > 0:
                    break
                ans[0] += 1
            elif rindex == 0:
                yindex += 1
                if rindex > 0 and yindex > 0:
                    break
                ans[1] += 1
        except IndexError:
            break


    return f'{ans[0]} {ans[1]}'





if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(f'Case #{i+1}: {solve()}')