N = int(input())
num = ['3', '6', '9']
answer = ''

for i in range(1, N+1):
    cnt = 0
    for j in str(i):
        if(j in num):
            cnt += 1
    if(cnt == 0):
        answer += str(i)
    else:
        for l in range(cnt):
            answer += '-'
    answer += ' '

print(answer)