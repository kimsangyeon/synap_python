def gogo():
    setA = set(map(int, input().split()))
    for i in range(int(input())):
        setB = set(map(int, input().split()))
        if(setA.intersection(setB) != setB):
            print("False")
            return

    print("True")


gogo()

