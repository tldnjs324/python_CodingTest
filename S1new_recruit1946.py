import sys

T = int(sys.stdin.readline()) #테스트 수

for i in range(T):
    N = int(input()) #한 테스트의 지원자 수
    count = 1
    applicants = [] #지원자 저장 배열
    for i in range(N):
        document, interview = map(int, sys.stdin.readline().split()) #서류, 인터뷰 받아오기(input 시간 초과돼서 변경)
        applicants.append([document, interview]) #배열 뒤에 추가

    applicants.sort() #서류 기준으로 오름차순 정렬
    min = applicants[0][1] #서류 꼴등

    for i in range(1, N):
        if min > applicants[i][1]:
            count += 1
            min = applicants[i][1]

    print(count)

