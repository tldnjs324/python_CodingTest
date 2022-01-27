#입력받을 컴퓨터의 수 n,
n = int(input())
#네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수 m
m = int(input())

#경로를 저장하기 위한 2차원 리스트
graph = [[] * n for _ in range(n + 1)]
#방문 처리
visited = [False] * (n + 1)
#다녀간 정점을 확인하기 위한 변수 count
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    global count #전역 변수로 바꿔줌
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(i)
            count += 1

dfs(1)
print(count)