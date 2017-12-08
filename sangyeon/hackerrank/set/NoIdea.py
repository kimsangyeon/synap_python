n, m = raw_input().split()
arr = map(int, raw_input().split())
a = set(map(int, raw_input().split()))
b = set(map(int, raw_input().split()))

count = [1 if x in a else -1 if x in b else 0 for x in arr]

print(sum(count))