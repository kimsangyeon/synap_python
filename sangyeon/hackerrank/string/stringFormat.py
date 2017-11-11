def print_formatted(number):
    width = len(replace_formatted(bin(number)))
    for i in range(0, number):
        print(str(i + 1).rjust(width, ' ') + ' ' + replace_formatted(str(oct(i + 1))).rjust(width, ' ') + ' ' + replace_formatted(str(hex(i + 1))).rjust(width, ' ') + ' ' + replace_formatted(str(bin(i + 1))).rjust(width, ' '))
        
def replace_formatted(n):
    if n.find('0o') == 0:
        n = n.replace('0o', '')
    elif n.find('0x') == 0:
        n = n.replace('0x', '').upper()
    elif n.find('0b') == 0:
        n = n.replace('0b', '')
    return n

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)