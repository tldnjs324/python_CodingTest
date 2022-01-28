from collections import deque
import sys
#행의 수 R, 열의 수 C
R, C = map(int, input().split())
#마당
yard = []
#방문 처리를 2차원 리스트로
visited = [[False]*C for _ in range(R)]
#양o, 늑대v 초기화
o, v = 0, 0

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global o, v
    queue = deque()
    queue.append([x, y])
    #늑대 카운트, 양 카운트
    sheep, wolf = 0, 0
    if yard[x][y] == "o":
        sheep += 1
    elif yard[x][y] == "v":
        wolf += 1

    while queue:
        x, y = queue.popleft()
        #현재 위치에서 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위 내에 있고, 방문하지 않았으며, 울타리가 아닐 때 양과 늑대 세기
            if 0<= nx < R and 0<= ny <C and not visited[nx][ny] and yard[nx][ny]!="#":
                if yard[nx][ny] == "o":
                    sheep += 1
                if yard[nx][ny] == "v":
                    wolf += 1
                visited[nx][ny] = True
                queue.append([nx, ny])
    #울타리 안에 양이 많다면 그 울타리 안의 늑대 수를 빼고, 아님 양의 수 뺌
    if sheep and wolf:
        if sheep > wolf:
            v -= wolf
        else:
            o -= sheep

#마당 입력 받기
for i in range(R):
    yard.append(list(input().rstrip()))
#마당에 있는 양 수, 늑대 수 세기
for i in range(R):
    #a = list(input().strip())
    for j in range(C):
        if yard[i][j] == "o":
            o += 1
        if yard[i][j] == "v":
            v += 1

for i in range(R):
    for j in range(C):
        if(yard[i][j] == "o" or yard[i][j] == "v") and not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)

print(o, v)



