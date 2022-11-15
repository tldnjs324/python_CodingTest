T = int(input())

for tc in range(1, T + 1):

    text = input()
    patten = []
    next_patten = []
    ans = 0

    for i in range(11):
        patten = text[:i]
        next_patten = text[i:i * 2]
        # print(patten)
        # print(next_patten)
        if i != 0 and patten == next_patten:
            ans = len(patten)
            break

    print('#{} {}'.format(tc, ans))