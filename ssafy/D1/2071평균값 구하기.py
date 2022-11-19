T = int(input())
for i in range(T):
    nums = list(map(int, input().split()))
    print("#%d %d" % (i+1, round(sum(nums)/10)))
