def print_rangoli(size):
    width = size * 4 - 3
    for i in range(size , 0, -1):
        alpha = chr(96 + size)
        for j in range(size - 1, i - 1, -1):
            alpha += '-' + chr(96 + j)
        for k in range(i + 1, size + 1):
            alpha += '-' + chr(96 + k)
        print(alpha.center(width,'-'))
    for i in range(2, size + 1):
        alpha = chr(96 + size)
        for j in range(size - 1, i - 1, -1):
            alpha += '-' + chr(96 + j)
        for k in range(i + 1, size + 1):
            alpha += '-' + chr(96 + k)
        print(alpha.center(width,'-'))