n = int(input())

words = []
Ks = []
for i in range(n):
    take = str(input()).split()
    K = take[1]
    letters = str(input())
    words.append(letters)
    Ks.append(int(K))

out = []
for x in range(len(words)):
    good = 0
    for i in range(len(words[x])//2):
        if words[x][i] != words[x][len(words[x])-1-i]:
            good += 1
    out.append(f"Case #{x+1}: {abs(Ks[x]-good)}")

for thing in out:
    print(thing)