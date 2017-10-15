if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tp = tuple(list(integer_list))
    print(hash(tp))
