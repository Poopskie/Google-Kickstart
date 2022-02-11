t = int(input())

color = ['U', 'R', 'Y', 'B', 'O', 'P', 'G', 'A']
value = [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]


convert = {x:y for x, y in zip(color, value)}

final = []

for i in range(t):
    ans = 0
    n = int(input())
    s_old = str(input())
    s = []

    convert = {'U': [], 'R': [1], 'Y': [2], 'B': [3], 'O': [1, 2], 'P': [1, 3], 'G': [2, 3], 'A': [1, 2, 3]}

    for x in range(n):
        s.append(s_old[x])
    for j in range(n):
        s[j] = convert[s_old[j]].copy()

    done = 0

    while done <= n-1:
        for x in range(1,4):
            try:
                temp_done = done
                s[temp_done].remove(x)
                while True:
                    try:
                        temp_done += 1
                        s[temp_done].remove(x)
                    except ValueError:
                        break
                    except IndexError:
                        break
                ans += 1
            except ValueError:
                continue
        done += 1
        
    final.append(ans)

for i in range(t):
    print(f"Case #{i+1}: {final[i]}")





