#입력 받을 물건의 가격
price = int(input())
#동전 개수
count = 0

#큰 단위의 화폐부터 차례로 확인
coin_types = [500, 100, 50, 10, 5, 1]
#거스름돈
change = 1000-price

for coin in coin_types:
    count += change // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    change %= coin

print(count)