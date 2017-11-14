def minion_game(string):
    vowels = 'AEUIO'

    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if stuart > kevin:
        print("Stuart " + str(stuart))
    elif stuart < kevin:
        print("Kevin " + str(kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)