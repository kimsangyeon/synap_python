for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    bSubSet = True
    for a in A:
        if a not in B:
            bSubSet = False
    print(bSubSet)
        