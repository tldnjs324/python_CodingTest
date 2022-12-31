T = int(input())
for tc in range(1, T+1):
    h1, h2 = map(int, input().split())
    h3 = h1 + h2
    if h3 >= 24:
        h3 -= 24
    elif h3 == 48:
        h3 = 0
    print('#{} {}'.format(tc, h3))