def swap_case(s):
    swap = ''
    for a in s:
        if a.isalpha():
            if 65 <= ord(a) and ord(a) <= 90:
                swap += a.lower()
            elif 97<= ord(a) and ord(a) <= 122:
                swap += a.upper()
        else:
            swap += a
    return swap