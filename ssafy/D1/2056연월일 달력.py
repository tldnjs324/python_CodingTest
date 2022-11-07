T = int(input())

days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for test_case in range(1, T + 1):
    case = str(input())
    year = case[0:4]
    month = case[4:6]
    day = case[6:8]

    answer = ''
    if 0 < int(month) < 13 and 0 < int(day) <= days[int(month)]:
        answer = year + '/' + month + '/' + day
    else:
        answer += '-1'

print("#" + str(test_case) + " " + answer)