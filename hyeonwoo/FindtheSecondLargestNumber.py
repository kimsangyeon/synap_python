if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    sortedArr = sorted(arr)

    largestItem = sortedArr[n-1]

    while sortedArr[n-1] >= largestItem:
        n = n-1

    print(sortedArr[n-1])
