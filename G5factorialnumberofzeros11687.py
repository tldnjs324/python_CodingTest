#가장 끝의 0의 개수가 M개인 N!
M = int(input())
start, end = 1, M*5 #M을 5배를 하면 (M*5)!은 5가 최소 M개는 나오기에 최대값으로 설정
result = 0 #가장 끝의 0의 개수가 M개인 N! 중에서 가장 작은 N

while start <= end:
    mid = (start+end)//2
    num = 0
    temp = mid
    while (temp >= 5):
        num += temp//5
        if(num >= M):
            break
        temp //= 5

    if(num >= M):
        end = mid - 1
        result = mid
    else:
        start = mid + 1


if(result == 0):
    print(-1)
else:
    print(result)
