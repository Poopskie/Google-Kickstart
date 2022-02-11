t = int(input())



def solve():
    ans = 0
    n = int(input())
    poo = str(input())

    inters = []

    for i in range(n):
        if poo[i] == '1':
            inters.append(i)

    for i in range(n):
        lowest = 100000000
        if poo[i] == '0':
            inters.append(i)
            inters.sort()
            for j in range(-1,2,2):
                try:
                    if abs(inters[inters.index(i)] - inters[inters.index(i)-j]) < lowest:
                        lowest = abs(inters[inters.index(i)] - inters[inters.index(i)-j])
                except IndexError:
                    continue
            inters.remove(i)

            ans += lowest



    return ans



for i in range(t):
    print(f"Case #{i+1}: {solve()}" )








