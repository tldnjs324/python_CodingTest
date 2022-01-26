from collections import deque

#N까지의 텔레포트 정거장, 텔레포트 연결 정보 M줄
N, M = map(int, input().split())
#만나는 지점 S, 방주가 있는 점 E
S, E = map(int, input().split())

teleport = [[]for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    x, y = map(int, input().split())
    teleport[x].append(y)
    teleport[y].append(x)

def bfs(start):
    queue = deque()
    queue.append((start, 0))
    while queue:
        x, d = queue.popleft()
        if x == E:
            return d
        if 1<= x <= N:
            if not visited[x]:
                visited[x] = True
                queue.append((x+1, d+1))
                queue.append((x-1, d+1))
                if len(teleport[x]) > 0:
                    for i in teleport[x]:
                        queue.append((i, d+1))

print(bfs(S))

