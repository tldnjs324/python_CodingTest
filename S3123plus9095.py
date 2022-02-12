#테스트 케이스 개수 T
T = int(input())
#1,2,3으로 1을 만들 수 있는 방법의 수, 2를 만들 수 있는 방법의 수, 3을 만들 수 있는 방법의 수, ...
nums = [1, 2, 4]
#4번째 부터 추가(-1위치에서의 합, -2위치에서의 합, -3위치에서의 합을 더하면 현재 수를 만들 수 있는 방법의 수가 된다.
for i in range(3, 10):
    nums.append(nums[i - 3] + nums[i - 2] + nums[i - 1])
#T개의 n을 입력받은 후 출력
for i in range(T):
    n = int(input())
    print(nums[n - 1])