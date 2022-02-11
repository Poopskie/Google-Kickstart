t = int(input())

alpha = "abcdefghijklmnopqrstuvwxyz"
final = []

for i in range(t):
    ans = 0
    s = input()
    f = input()

    for x in range(len(s)):
        min = 25
        uno = alpha.find(s[x])
        for y in range(len(f)):
            duos = alpha.find(f[y])
            if abs(uno - duos) < min:
                min = abs(uno - duos)
            if abs(uno - (duos+26)) < min:
                min = abs(uno - (duos+26))
            if abs((uno+26) - duos) < min:
                min = abs((uno+26) -duos)
        ans += min
    final.append(ans)

for i in range(t):
    print(f"Case #{i+1}: {final[i]}")














