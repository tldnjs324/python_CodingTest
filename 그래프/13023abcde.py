import sys

n, m = map(int, input().split())
arr = [[] for i in range(n)]
visited = [False] * n

# 그래프를 인접 리스트 방식으로 표현
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(idx, number):
    if number == 4:
        print(1)
        exit()
    for i in arr[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, number + 1)
            visited[i] = False

# 노드를 순서대로 방문하며 dfs를 수행
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)