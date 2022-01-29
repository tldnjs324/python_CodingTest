from collections import deque
#지도 크기 N(정사각형)
N = int(input())
#지도 이차원 리스트로
field = []
for i in range(N):
    field.append(list(map(int, input())))

num = []
count = 0

#상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    global count
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if field[x][y] == 1:
        count += 1
        field[x][y] = 0
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True
    #return False

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            num.append(count)
            count = 0

num.sort()
print(len(num))
for i in num:
    print(i)
