#일직선으로 놓여진 N개의 화분, 초기에 머금고 있는 수분의 양 K, 물을 줄 연속된 화분의 수 A, B만큼 증가 할 화분의 수분
N, K, A, B = map(int, input().split())

bases = list(range(0, N))
day = 0
a = 0 #연속해서 줄 화분의 첫번재 인덱스

for i in range(N):
    bases[i] = K

while True:
    day += 1

    for i in range(a, a+A+1):
        bases[i] += B
    a += A
    if a >= N:
        a = 0

    for i in range(N):
        bases[i] -= 1
        if bases[i] == 0:
            print(day)
            break




