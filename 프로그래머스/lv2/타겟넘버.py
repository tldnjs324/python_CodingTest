def solution(numbers, target):
    answer = 0
    #계산 결과를 담을 리스트 nums
    nums = [0]
    #numbers들을 차래대로 앞서 계산한 값들에 더하고, 빼면서 계산 결과를 갱신 시킨다
    for i in numbers:
        temp = []
        for j in nums:
            temp.append(j + i)
            temp.append(j - i)
        nums = temp

    #계산 결과에 타겟 넘버가 있다면 답에 1을 더한다
    for i in nums:
        if i == target:
            answer += 1