import operator
if __name__ == '__main__':
    dict = {}
    scoreArr = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        dict[name] = score
        scoreArr.append(score)

    sortedScore = sorted(list(set(scoreArr)))
    secondLowest = sortedScore[1]

    sortedArr = sorted(dict.items(), key= operator.itemgetter(1,0))

    for i in range(n):
        if sortedArr[i][1] == secondLowest:
            print(sortedArr[i][0])