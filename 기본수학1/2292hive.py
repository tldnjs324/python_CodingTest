n = int(input())

hive_num = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > hive_num:
    hive_num += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)