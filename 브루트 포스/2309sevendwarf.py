n = 9
temp1, temp2 = 0, 0
arr = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            temp1 = arr[i]
            temp2 = arr[j]

arr.remove(temp1)
arr.remove(temp2)

print('\n'.join(map(str, sorted(arr))))
