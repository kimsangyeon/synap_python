n = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

unionSet = a.union(b)
intersectionSet = a.intersection(b)

valSet = unionSet.difference(intersectionSet)

valList = list(valSet)
valList.sort()
for i in range(len(valList)) :
    print(valList[i])