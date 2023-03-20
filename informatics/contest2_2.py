a = input().split()
b = input().split()
c = input().split()
lst = []
for i in b:
    if i in c and i not in a:
        lst.append(int(i))
print(sorted(lst))