N = int(input())
num = ['3', '6', '9']
for i in range(1, N+1):
    cnt = 0
    for j in str(i):
        if(j in num):
            cnt += 1
    if(cnt > 0):
        print('-', end=' ')
    else:
        print(i, end=' ')