def dfs(x, y):
    #주어진 범위를 벗어나는 경우에는 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    # 현재 노드를 아직 방문하지 않았다면 해당 노드 방문 처리
    if field[x][y] == 1:
        field[x][y] = 0
        #상, 하, 좌, 우의 위치들 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y + 1)
        return True
    return False

#테스트의 케이스 개수 T
T = int(input())

for _ in range(T):
    #가로길이 M, 세로길이 N, 배추가 심어져 있는 위치의 개수 K
    M, N, K = map(int, input().split())
    #배추의 위치 Field
    field = [[0] * M for i in range(N)]
    #배추 지렁이 수
    count = 0
    #K개의 배추 위치에 배추 심기
    for _ in range(K):
        a, b = map(int, input().split())
        field[b][a] = 1
    for i in range(N):
        for j in range(M):
            #배추가 존재한다면, 인접 배추를 탐색하고, 탐색한 배추는 0, 지렁이 수를 늘린다
            #if field[i][j] == 1:
            if dfs(i, j):
                #field[i][j] = 0
                count += 1
    print(count)