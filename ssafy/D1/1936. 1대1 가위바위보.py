a, b = map(int, input().split())

#a가 이기는 경우
if(a == 1 and b == 3) or (a == 2 and b ==1) or (a == 3 and b == 2):
    print('A')
#b가 이기는 경우
else:
    print('B')