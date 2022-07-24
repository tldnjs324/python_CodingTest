#n! 할 n
n = int(input())

#0의 개수
cnt = 0

#n을 5로 나눈 몫이 n!의 0의 개수.
while n > 0:
  cnt += n//5 #
  n //= 5

#0의 개수 출력
print(cnt)