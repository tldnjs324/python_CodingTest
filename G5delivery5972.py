import heapq

INF = int(1e9)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dis[start] = 0
    while queue:
        d, now = heapq.heappop(queue)
        if dis[now] < d:
            continue
        for i, j in graph[now]:
            cost = d + j
            if cost < dis[i]:
                dis[i] = cost
                heapq.heappush(queue, (cost, i))

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

dis = [INF]*(N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dijkstra(1)

print(dis[N])
