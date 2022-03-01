import heapq

N = int(input())
room = [list(map(int, input())) for _ in range(N)]
graph = [[0]*N for _ in range(N)]

def dijkstra():
    heap = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    heapq.heappush(heap, [0, 0, 0])
    graph[0][0] = 1

    while heap:
        a, x, y = heapq.heappop(heap)
        if x == N-1 and y == N-1:
            print(a)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny <N and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                if room[nx][ny] == 0:
                    heapq.heappush(heap, [a+1, nx, ny])
                else:
                    heapq.heappush(heap, [a, nx, ny])

dijkstra()