#나무의 수 N, 상근이가 집으로 가져가려고 하는 나무의 길이 M
N, M = map(int, input().split())
#나무의 높이
tree = list(map(int, input().split()))
# 이분탐색 검색 범위 설정
start, end = 1, max(tree)

#적절한 벌목 높이를 찾는 알고리즘
while start <= end:
    mid = (start + end) // 2

    # 벌목된 나무 총합
    log = 0
    for i in tree:
        if i >= mid:
            log += i - mid

    #벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)