#집의 개수 N, 공유기의 개수 C
N, C = map(int, input().split())

#집들의 좌표를 받을 배열
array = []
for i in range(N):
    array.append(int(input()))
#배열을 오름차순으로 정렬
array.sort()

first = 1 #시작 값 최소 거리
last = array[N-1] - array[0] #끝 값 최대 거리

#이진탐색
while first <= last:
    mid = (first + last) // 2  # 최소 거리와 최대 거리의 중앙 값
    pivot = array[0]  # 마지막으로 공유기를 설치한 좌표
    count = 1  # 설치한 공유기 수

    for i in range(1, len(array)):
        if array[i] >= pivot + mid:
            count += 1
            pivot = array[i]

    # 설치한 공유기 수가 C개와 같거나 많다면 더 넓게 설치해야 함으로 mid+1로 다시 설치한다
    if count >= C:
        first = mid + 1
        result = mid  # result는 최대 거리가 된다.
    # 설치한 공유기 수가 C개 보다 적다면 공유기를 더 좁게 설치해야 함으로 mid-1로 다시 설치한다.
    else:
        last = mid - 1

print(result)