n = input();
s = set(map(int, input().split()));
n = input();
print(len(s.intersection(set(map(int, input().split())))))