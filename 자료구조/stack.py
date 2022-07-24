import sys

#첫째 줄에 주어지는 명령의 수 N
N = int(sys.stdin.readline())

stack = []

#for문으로 N개 명령어 받기
for _ in range(N):
    # split으로 입력 받기
    word = sys.stdin.readline().split()

    #명령어가 push 라면
    if word[0] == 'push':
        stack.append(int(word[1]))#두 번째 입력어를 push
    #명령어가 pop 일 때
    elif word[0] == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    #명령어가 top 일 때
    elif word[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    # 명령어가 size 일 때
    elif word[0] == 'size':
        print(len(stack))#스택에 들어있는 정수 개수 출력
    # 명령어가 empty 일 때
    elif word[0] == 'empty':
        if len(stack) > 0: #비어있지 않으면 0
            print(0)
        else: #비어있으면 1
            print(1)