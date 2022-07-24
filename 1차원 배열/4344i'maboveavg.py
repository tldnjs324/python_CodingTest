num = int(input())

for _ in range(num):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0] #1번째 요소부터 마지막 요소까지 sum을 이용하여 더한 다음, 학생의 수인 scores[0]으로 나눔

    cnt = 0
    for i in scores[1:]:
        if i > avg:
            cnt += 1

    per = (cnt / scores[0]) * 100
    print('%.3f' % per + '%')