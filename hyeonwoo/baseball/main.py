import random

# 맞춰야할 랜덤 숫자 생성
ran_num = ["0", "0", "0"]
ran_num[0] = str(random.randrange(1, 9, 1))
ran_num[1] = ran_num[0]
ran_num[2] = ran_num[0]
# 같은 숫자가 없어야 하기때문에 한 개씩 생성
while (ran_num[0] == ran_num[1]):
    ran_num[1] = str(random.randrange(1, 9, 1))
while (ran_num[0] == ran_num[2] or ran_num[1] == ran_num[2]):
    ran_num[2] = str(random.randrange(1, 9, 1))

t_count = 0  # 횟수
s_count = 0  # 스트라이크
b_count = 0  # 볼

print("\n")
while (s_count < 3):
    num = str(input("숫자 3자리를 입력하세요. ex)123 : "))
    if (num == ""):
        print("\n\n숫자를 입력해주세요. \n\n")
        continue
    if (len(num) != 3):
        print("\n\n숫자 3자리만 입력해주세요.\n\n")
        continue
    if (num.isalpha()):
        print("\n\n문자를 입력할 수 없습니다.\n\n")
        continue

    s_count = 0
    b_count = 0

    for i in range(0, 3):
        for j in range(0, 3):
            if (num[i] == str(ran_num[j]) and i == j):
                s_count += 1
            elif (num[i] == str(ran_num[j]) and i != j):
                b_count += 1
    print("\n[", s_count, "] 스트라이크! [", b_count, "] 볼!\n")
    t_count += 1
print(t_count, "번 만에 3스트라이크!!")