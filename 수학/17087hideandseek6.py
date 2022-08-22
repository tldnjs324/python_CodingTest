import math

N, S = map(int, input().split())
A = list(map(int, input().split()))
ck = []

ans = 1000000000
for i in A:
    ck.append(abs(i - S))

ans = ck[0]
for i in range(1, N):
    ans = math.gcd(ck[i], ans)

print(ans)