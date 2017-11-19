def minion_game(string):
    aCol = ['A', 'E', 'I', 'O', 'U'];
    
    sScore = 0;
    kScore = 0;
    
    for i in range(0, len(string)):
        if string[i] in aCol:
            for j in range(i + 1, len(string) + 1):
                kScore += 1;
        else:
            for j in range(i + 1, len(string) + 1):
                sScore += 1;
    
    if sScore > kScore:
        print('Stuart %d' % sScore);
    elif kScore > sScore:
        print('Kevin %d' % kScore);
    else:
        print('Draw');