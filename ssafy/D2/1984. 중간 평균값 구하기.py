T = int(input())
for tt in range(T):
    a = list(map(int, input().split()))
    print( "#%d %d" % (tt+1, round( (sum(a)-max(a)-min(a))/8)) )