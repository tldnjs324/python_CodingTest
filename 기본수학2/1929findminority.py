M, N = map(int, input().split()) #M이상 N이하의 소수를 찾을 M, N

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1): #2부터 i의 제곱근까지만 검사하면 됨
            if num%i == 0:
                return False
        return True

for i in range(M, N+1):
    if isPrime(i):
        print(i)