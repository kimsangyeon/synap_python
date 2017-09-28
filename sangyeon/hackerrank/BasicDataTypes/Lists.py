if __name__ == '__main__':
    N = int(input())
    commandList = []
    numList = []
    for i in range(0, N):
        tmp = str(input()).split(' ')
        command = tmp[0]
        if command == 'insert':
            numList.insert(int(tmp[1]), int(tmp[2]))
        elif command == 'append':
            numList.append(int(tmp[1]))
        elif command == 'remove':
            numList.remove(int(tmp[1]))
        elif command == 'sort':
            numList.sort()
        elif command == 'reverse':
            numList.sort(reverse=True)
        elif command == 'pop':
            numList.pop()
        elif command == 'print':
            print(numList)