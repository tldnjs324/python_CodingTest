import sys
import queue

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            elif graph[j][i] and graph[i][k]:
                if graph[j][k] == 0:
                    graph[j][k] = graph[j][i] + graph[i][k]
                else:
                    graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
for i in range(n):
    result = 0
    for j in range(n):
        result += graph[i][j]
    if INF > result:
        INF = result
        person = i

print(person+1)