T = int(input()) #테스트 케이스 개수 T

for _ in range(T):
    R, S = input().split() #반복 횟수 R, 문자열 S
    for x in S:
        print(x*int(R), end='')  # end='' 옆으로 붙임
    print()  # 줄넘김