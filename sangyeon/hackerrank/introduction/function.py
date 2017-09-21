def is_leap(year):
    leap = False
    
    if year%4 is 0:
        leap = True
        if year%100 is 0:
            if year%400 is not 0:
                leap = False;
    
    return leap