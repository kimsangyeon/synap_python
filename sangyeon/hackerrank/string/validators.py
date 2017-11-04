if __name__ == '__main__':
    s = input()
    
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.isalpha() and c.islower() for c in s))
    print(any(c.isalpha() and c.isupper() for c in s))
    