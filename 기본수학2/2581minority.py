M = int(input()) #시작 숫자
N = int(input()) #마지막 숫자

minority_list = [] #소수 리스트
for num in range(M, N + 1):
    error = 0
    if num > 1:
        for i in range(2, num):  #2부터 num-1까지 수 중에서 num을 나눌 수 있는 수 찾기
            if num % i == 0:
                error += 1
                break  #2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄(소수 아님)
        if error == 0:
            minority_list.append(num)  #error가 없으면 소수리스트에 추가

if len(minority_list) > 0:
    print(sum(minority_list)) #소수 숫자
    print(min(minority_list)) #소수 중 최소값
else:
    print(-1) #소수가 없다면 -1