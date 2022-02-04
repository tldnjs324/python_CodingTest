def solution(n, times):
    answer = 0 # 모든 사람이 심사를 받는데 걸리는 시간의 최솟값
    # first는 가장 짦은 times, last는 가장 긴 times로 n명 모두가 검사했을 때 걸리는 시간
    first, last = min(times), max(times) * n

    #이진탐색
    while first <= last:
        mid = (first + last) // 2
        people = 0 # 모든 심사관들이 심사한 사람의 수
        for time in times:
            people += mid // time #mid분 동안 심사한 사람의 수를 더해준다
            # n명 이상의 사람을 심사를 할 수 있다면 for문을 나간다.
            if people >= n:
                break

        # 심사가 끝난 사람의 수가 n보다 많거나 같다면 최대 시간을 mid-1로 다시 심사한다
        if people >= n:
            answer = mid
            last = mid - 1
        # 심사가 끝난 사람의 수가 n보다 적다면 최소 시간을 mid+1로 다시 심사한다
        elif people < n:
            first = mid + 1

    return answer

n = int(input())
times = list(map(int, input().split()))
print(solution(n, times))
