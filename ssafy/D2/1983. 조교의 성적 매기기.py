T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split(' '))
    students = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for n in range(N):
        midterm, final, assignment = map(int, input().split())
        sum_student = midterm * 0.35 + final * 0.45 + assignment * 0.20
        students.append(sum_student)

    k_score = students[K-1]
    students.sort(reverse=True)

    rank_of_ten = students.index(k_score) // (N//10)
    k_grade = grade[rank_of_ten]

    print('#{} {}'.format(t, k_grade))