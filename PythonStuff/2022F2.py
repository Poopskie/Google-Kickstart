from itertools import permutations
from collections import Counter


def solve():
    l = list(map(int, input().split()))
    # l[0] = # of containers, l[1] = queries
    N = l[0]
    Q = l[1]
    connections = []
    for i in range(N-1):
        l1 = list(map(int, input().split()))
        connections.append(l1)
    for i in range(Q):
        input()

    

    # first, map out all the items
    # calculation: map to bottommost (1), if full
    # go to level above with dictionary of 1, then split between
    # them using len(dict[1]) - list of connections
    
    # MAP TO FIND WHAT LEVEL THEY ARE ON
    # JUST COUNT NUMBER OF QUERIES, IF > CONTAINERS ON LEVEL
    # THEN + CONTAINERS ON LEVEL (OTHERWISE NOT FULL)

    # list & dict constructors
    a = []
    for i in range(N):
        a.append([])

    connector = {key:value for key,value in zip(list(range(1,N+1)),a)}
    for i in range(N-1): # maps into eachothers list
        #can directly append to dict lists
        connector[connections[i][0]].append(connections[i][1])
        connector[connections[i][1]].append(connections[i][0])

    layers = [[1], connector[1]] # start with first 2 layers
    
    layernum = 1 # 2nd level --> layer 0, 1, 2...
    while True:
        layer = []
        for x in layers[layernum]: # if not in layer below, add to layer above
            for connection in connector[x]:
                # this is the list from the dict of a container on the layer
                if connection not in layers[layernum-1]:
                    layer.append(connection) # add those in next layer
        
        if layer == []: # end if layer empty
            break
        layers.append(layer)
        layernum += 1
    # this works so beautifully
    # I AM A FUCKING GENIUS

    # count shit
    layeron = 0
    ans = 0
    while True:
        try:
            if Q >= len(layers[layeron]):
                Q -= len(layers[layeron])
                ans += len(layers[layeron])
                layeron += 1
            else:
                break
        except:
            break
    return ans



if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print(f'Case #{i+1}: {solve()}')



