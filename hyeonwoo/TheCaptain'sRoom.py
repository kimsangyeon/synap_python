if __name__ == '__main__':
    k = int(input())
    arr = list(map(int,input().split()))

    setArr = set(arr)
    dic = dict()
    for x in arr:
        if x in dic:
            dic[x] = dic[x] + 1;
        else:
            dic[x] = 1;

        if dic[x] == k:
            setArr.remove(x)

    print(list(setArr)[0])