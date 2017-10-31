LOWER_CASE_A = 97
LOWER_CASE_Z = 122
UPPER_CASE_A = 65
UPPER_CASE_Z = 90

def swap_case(s):
    sList = []
    for c in s:
        sList.append(swap(c))
    
    return "".join(sList)

def swap(c):
    if UPPER_CASE_A <= ord(c) and ord(c) <= UPPER_CASE_Z:
        return c.lower()
    elif LOWER_CASE_A <= ord(c) and ord(c) <= LOWER_CASE_Z:
        return c.upper()
    return c

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)