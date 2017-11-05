
s = input()
f_check = False
for c in s:
    if c.isalnum():
        print("True")
        f_check = True
        break

if f_check == False:
    print("False")
f_check = False

for c in s:
    if c.isalpha():
        print("True")
        f_check = True
        break

if f_check == False:
    print("False")
f_check = False

for c in s:
    if c.isdigit():
        print("True")
        f_check = True
        break

if f_check == False:
    print("False")
f_check = False

for c in s:
    if c.islower():
        print("True")
        f_check = True
        break

if f_check == False:
    print("False")
f_check = False

for c in s:
    if c.isupper():
        print("True")
        f_check = True
        break

if f_check == False:
    print("False")
f_check = False
