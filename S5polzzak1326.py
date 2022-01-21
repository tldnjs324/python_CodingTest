def bfs(a, b, bridge, N):
    queue = deque()
    queue.append(a-1)

    # 각 노드가 방문된 정보를 표현(1차원 리스트)
    visited = [-1] * N
    # 현재 노드를 방문 처리
    visited[a - 1] = 0

    while queue:
        # 큐에서 하나의 원소를 뽑기
        v = queue.popleft()
        for i in range(N):
            if(i-v)%bridge[v] == 0 and visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v]+1
                if i == b-1:
                    return visited[i]

from collections import deque

#징검다리의 개수 N
N = int(input())
#각 징검다리에 쓰여 있는 N개의 정수 리스트
bridge = list(map(int, input().split()))
#a번째 징검다리에서 b번째 징검다리까지
a, b = map(int, input().split())

print(bfs(a, b, bridge, N))