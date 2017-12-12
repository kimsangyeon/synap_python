setA = set(map(int, input().split()))

bStrictSuperSet = True
for _ in range(int(input())):
    setN = set(map(int, input().split()))
    for n in setN:
        if n not in setA:
            bStrictSuperSet = False
            break
print(bStrictSuperSet)
    