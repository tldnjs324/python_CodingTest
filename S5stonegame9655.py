#입력 받는 N개의 돌
N = int(input())
#N이 홀수이면 SK가 이기고, N이 짝수이면 CY가 이긴다.
if N % 2 == 0:
    print("CY")
else:
    print("SK")