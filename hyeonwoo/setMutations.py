n = int(input())
A =  set(list(map(int, input().split())))
N = int(input())

for i in range(N):
    cmd = list(input().split())
    operate = cmd[0]
    setNum = set(list(map(int, input().split())))
    if operate == 'intersection_update':
        A.intersection_update(setNum)
    elif operate == 'update':
        A.update(setNum)
    elif operate == 'symmetric_difference_update':
        A.symmetric_difference_update(setNum)
    elif operate == 'difference_update':
        A.difference_update(setNum)

print(sum(A))