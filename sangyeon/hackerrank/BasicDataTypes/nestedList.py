if __name__ == '__main__':
    studentList = []
    scoreList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studentList.append([name, score])
        scoreList.append(score)

    secondScore = list(set(scoreList))
    secondScore.sort()
    
    nameList = []
    for name, score in studentList:
        if score == secondScore[1]:
            nameList.append(name)
    
    nameList.sort()
    for name in nameList:
        print(name)
