T = int(input())

for i in range(T):
    data = list(map(int, input().split()))
    sum = 0
    for j in range(10):
        if data[j]%2 == 1:
            sum+=data[j]

    print('#' + str(i+1), str(sum))
