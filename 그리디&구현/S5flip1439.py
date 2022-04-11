#입력 받을 문자열
data = input()
#변하는 지점 세는 변수
n = 0

for i in range(len(data)-1):
    if(data[i] != data[i+1]): #숫자가 달라졌다면
        n += 1 #변하는 지점 추가!
print((n+1)//2)#홀수일 때는 2로 나눈 몫의 +1이 되기 때문에 미리 +1을 해준다
