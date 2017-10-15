if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    t = tuple(list(integer_list))
    print(hash(t))
