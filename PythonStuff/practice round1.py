from itertools import permutations
from collections import Counter

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

def solve():
    global vowels
    name = str(input())
    if name[-1] in vowels:
        return f"{name} is ruled by Alice."
    elif name[-1].lower() != 'y':
        return f"{name} is ruled by Bob."
    else:
        return f"{name} is ruled by nobody."



if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(f"Case #{i+1}: {solve()}")



