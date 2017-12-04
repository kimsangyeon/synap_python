if __name__ == '__main__':
    n = int(raw_input())
    print(len(set([str(raw_input()) for _ in range(n)])))