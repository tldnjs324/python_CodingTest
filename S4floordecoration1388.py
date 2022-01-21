#방 바닥 세로 크기 N, 가로 크기 M
N, M = map(int, input().split())
floor = []
for i in range(N):
    floor.append(list(input()))
count = 0

#세로 장식 i
for i in range(N):
    j = 0
    while j<M:
        if floor[i][j] == '|':
            j += 1
        else:
            count += 1
            while j<M and floor[i][j] == '-':
                j += 1

#가로 장식 j
for j in range(M):
    i = 0
    while i<N:
        if floor[i][j] == '-':
            i += 1
        else:
            count += 1
            while i<N and floor[i][j] == '|':
                i += 1

print(count)