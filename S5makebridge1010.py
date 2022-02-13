import math
#테스트 케이스 개수
T = int(input())

#테스트 케이스 개수 만큼 n, m을 입력 받고, 조합을 이용해 다리의 개수를 구한다.
for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)