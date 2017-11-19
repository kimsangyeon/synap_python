def merge_the_tools(string, k):
    for i in range(int(len(string)/k)) :
        subStr = string[i*k:(i+1)*k]
        setStr = set(subStr)
        resultStr = []
        for j in range(k):
            if subStr[j] in setStr :
                resultStr.append(subStr[j])
                setStr.remove(subStr[j])
            if len(setStr) == 0:
                for l in range(len(resultStr)):
                    print(resultStr[l],end="")
                print()
                break



string, k = input(), int(input())
merge_the_tools(string, k)