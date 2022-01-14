#물이 새는 곳의 개수 N과 테이프의 길이 L을 입력받음
N, L = map(int, input().split())
#물의 새는 곳의 위치를 N개 입력받음
location = list(map(int, input().split()))
location.sort()
count = 0
start = 0

for loc in location:
    if start<loc: #수리해야 할 위치가 시작 위치보다 크면(시작 위치 보다 작다면 이미 테이프가 붙어있음)
        start = loc+L-1 #테이프를 붙이고, 시작 위치를 테이프가 붙어있는 마지막 위치로 정함
        count += 1
print(count)