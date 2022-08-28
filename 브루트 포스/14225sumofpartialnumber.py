#수열 s의 크기 n
n = int(input())
#수열 S
s = list(map(int, input().split()))

a = 0

#수열 s를 정렬해서
for i in [*sorted(s)]:
    if a+1 < i:
        break
    a += i

print(a+1)
