#입력 받을 설탕의 kg
kg = int(input())
#설탕 봉지 수
count = 0

#kg이 0이상인 경우 실행
while kg>=0:
    if kg%5 == 0: #5로 나눈 나머지가 0이라면
        count += kg//5 #5로 나눈 몫을 봉지수에 플러스
        print(count)
        break
    kg -= 3 #5로 나눠지지 않으면 -3해서 5 배수 될 때까지 반복
    count += 1 #3kg 봉지 추가
else:
    print(-1)#kg이 음수가 되면 5와 3으로 떨어지지 않는거라서 틀림 