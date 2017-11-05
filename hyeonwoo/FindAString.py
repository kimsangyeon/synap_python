def count_substring(string, sub_string):
    i=0
    string_len = len(string)
    sub_len = len(sub_string)
    count = 0
    while 1:
        i = string.find(sub_string, i)
        if i < 0:
            break

        i = i + 1;
        count = count + 1

        if i > string_len:
            break

    return count

string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)