import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    word = sys.stdin.readline().split()
    if word[0] == 'push':
        stack.append(int(word[1]))
    elif word[0] == 'top':
        if len(stack) > 0: print(stack[-1])
        else: print(-1)
    elif word[0] == 'pop':
        if len(stack) > 0: print(stack.pop())
        else: print(-1)
    elif word[0] == 'size':
        print(len(stack))
    elif word[0] == 'empty':
        if len(stack) > 0: print(0)
        else: print(1)