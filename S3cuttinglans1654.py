import sys

#오영식이 이미 가지고 있는 랜선의 개수 K, 필요한 랜선의 개수 N
K, N = map(int, input().split())
#K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이를 입력받음
lan = [int(sys.stdin.readline()) for _ in range(K)]
#이분탐색 처음과 끝위치
start, end = 1, max(lan)  

#적절한 랜선의 길이를 찾는 알고리즘
while start <= end:  
    mid = (start + end) // 2 #중간 위치
    lines = 0 #랜선 수
    #잘린 랜선 수
    for i in lan:
        lines += i // mid

    #잘린 랜선의 수와 필요한 랜선의 수 비교
    if lines >= N:  
        start = mid + 1
    else:
        end = mid - 1
print(end)