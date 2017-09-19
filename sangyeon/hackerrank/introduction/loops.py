if __name__ == '__main__':
    n = int(input())

    sum = 0
    odd = 1
    for i in range(0, n):
        print(sum)
        sum += odd
        odd += 2