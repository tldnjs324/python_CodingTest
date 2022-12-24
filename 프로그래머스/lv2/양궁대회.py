def solution(n, info):
    answer = [0] * 11
    arr = [0] * 11
    maxDiff = 0

    for subset in range(1, 1 << 10):
        ryan = 0
        peach = 0
        cnt = 0

        for i in range(10):
            if subset & (1 << i):
                ryan += 10 - i
                arr[i] = info[i] + 1
                cnt += arr[i]
            else:
                arr[i] = 0
                if info[i]:
                    peach += 10 - i

        if cnt > n: continue

        arr[10] = n - cnt

        if ryan - peach == maxDiff:
            for j in reversed(range(11)):
                if arr[j] > answer[j]:
                    maxDiff = ryan - peach
                    answer = arr[:]
                    break
                elif arr[j] < answer[j]:
                    break

        elif ryan - peach > maxDiff:
            maxDiff = ryan - peach
            answer = arr[:]

    if maxDiff == 0:
        answer = [-1]
    return answer