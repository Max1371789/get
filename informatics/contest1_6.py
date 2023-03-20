def rabin_karp(x,y):
    positions = []
    for i in range(len(y)-len(x)+1):
        if hash(x) == hash(y[i:i+len(x)]):
            positions.append(i)
    if positions != []:
        return print(*positions)
    else:
        return print(-1)
a = input()
b = input()
rabin_karp(a,b)





