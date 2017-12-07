n = input()
s1 = set(map(int, raw_input().split()))
n = input()
s2 = set(map(int, raw_input().split()))

result = s1.union(s2)

print(len(result))