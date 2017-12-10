n = int(input())
setA = set(map(int, input().split()))
m = int(input())
setB = set(map(int, input().split()))

print(len(setA.union((setB))))