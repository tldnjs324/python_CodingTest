from math import factorial

n = int(input())

cnt = 0

# n 팩토리얼을 계산한 뒤, str로 바꿔주고 뒤집음
# 0이 나오지 않을 때까지 0의 개수를 더해주며 반복문을 돌림
for x in str(factorial(n))[::-1]:
    if x != '0':
        break
    cnt += 1

print(cnt)