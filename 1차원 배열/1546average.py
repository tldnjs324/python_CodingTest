n = int(input())  #과목 수
test_list = list(map(int, input().split())) #시험 점수 리스트
max_score = max(test_list) #최대값

new_list = [] #조작할 리스트
for score in test_list:
    new_list.append(score/max_score *100)  #새로운 점수 만들어서 추가
test_avg = sum(new_list)/n
print(test_avg)