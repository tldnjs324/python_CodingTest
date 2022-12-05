from collections import defaultdict


def solution(fees, records):
    answer = []
    parking_lot = {}
    time_dict = defaultdict(int)

    for record in records:
        time, num, status = record.split(' ')
        if status == 'IN':
            parking_lot[num] = time
        else:
            h1, m1 = map(int, parking_lot[num].split(':'))
            h2, m2 = map(int, time.split(':'))
            times = ((h2 - h1) * 60) + m2 - m1
            time_dict[num] += times
            del parking_lot[num]

    for num, time in parking_lot.items():
        h1, m1 = map(int, parking_lot[num].split(':'))
        time_dict[num] += ((23 - h1) * 60) + 59 - m1

    for num, time in sorted(time_dict.items()):
        answer.append(fees[1])
        if time > fees[0]:
            time -= fees[0]
            overtime = time // fees[2]
            if time % fees[2]:
                overtime += 1
            answer[-1] += (overtime * fees[3])

    return answer
