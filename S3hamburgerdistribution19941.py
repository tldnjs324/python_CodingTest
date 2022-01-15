# 식탁의 길이 N, 햄버거를 선택할 수 있는 거리 K 입력 받음
N, K = map(int, input().split())
#H랑 P 입력받기
tables = list(input())
count = 0

for i in range(N):
    if tables[i] == "P": #리스트에서 P 찾아서
        for j in range(i-K, i+K+1): #P에서 K만큼 떨어진 곳 중 가장 앞에 있는 곳에서 부터 H를 찾는다
            if 0 <= j < N and tables[j] == "H": #H가 있다면
                count += 1 #i번째에 있는 사람은 햄버거를 먹을 수 있고, 
                tables[j] = "X" #그 곳의 햄버거는 없애버린다.
                break #그리고 다른 햄버거를 먹지 못하게 하기 위해 for문을 나온다

print(count)

