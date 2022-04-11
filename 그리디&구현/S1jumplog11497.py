T = int(input())

for i in range(T):
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort(reverse=True)#통나무를 내림차순으로 정렬
    result = 0
    for j in range(N-2):
        result = max(result, abs(logs[j+2]-logs[j]))
    print(result)