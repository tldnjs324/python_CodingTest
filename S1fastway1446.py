# 지름길 개수 N, 고속도로 길이 D
N, D = map(int, input().split())
#(시작위치, 도착위치, 지름길 길이)를 지름길 개수(N)번 입력 받는다
fw = [list(map(int, input().split())) for _ in range(N)]
# 최단거리 테이블 생성 [0, 1, 2, 3, .., D]
dis = [i for i in range(D+1)]

for i in range(D+1):
    # 한칸 전 위치의 테이블 값+1이 현재 테이블 값보다 작다면 현재 테이블 값을 한 칸 전 위치의 테이블 값+1로 변경
    if i>0:
        dis[i] = min(dis[i], dis[i-1]+1)
    for s, e, d in fw:
        # 현재 위치에 지름길이 있다면
        if i == s and e <= D and dis[i]+d < dis[e]:
            # 지름길로 건너간 곳의 원래 테이블 값과 지름길로 건너가기 전의 테이블값+지름길의 거리 중
            # 더 작은 값으로 건너간 곳의 값을 변경
            dis[e] = dis[i]+d

print(dis[D])