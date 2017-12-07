n = input()
s = set(map(int, raw_input().split())) 
cmdLength = input()

for _ in range(cmdLength):
    aCmd = map(str, raw_input().split())
    if(len(aCmd) > 1):
        eval('s.%s(%s)' % (aCmd[0], aCmd[1]))
    else:
        eval('s.%s()' % aCmd[0])

print(sum(s))