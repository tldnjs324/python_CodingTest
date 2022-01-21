def dfs(x, y, visited):
    if x >= N or x <= -1 or y >= N or y <= -1:
        return 0
    if visited[x][y] == True:
        return 0
    if map[x][y] == -1:
        print('HaruHaru')
        exit()
    visited[x][y] = True
    for i in range(2):
        nx = x + dx[i] * map[x][y]
        ny = y + dy[i] * map[x][y]
        dfs(nx, ny, visited)
    return True

#게임 구역의 크기 N
N = int(input())

#게임 맵 입력받기
map = []
for i in range(N):
    map.append(list(map(int, input().split())))

# 각 노드가 방문된 정보를 표현(2차원 리스트)
visited = []
for _ in range(N):
    visited.append([False] * N)

#하, 우
dx = [1, 0]
dy = [0, 1]

if dfs(0, 0, visited) == True:
    print('Hing')