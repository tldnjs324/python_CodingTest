words = input().upper() #입력 받을 단어
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words: #중복값 없앤 알파벳들에서
    cnt = words.count(x) #기존 단어에 해당 알파벳이 몇개인지 카운트
    cnt_list.append(cnt)  # unique_words의 해당 알파벳 수를 각각 cnt_list에 append

if cnt_list.count(max(cnt_list)) > 1:  # count 숫자 최대값이 중복되면
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))  # 카운트 리스트 최대값 위치(인덱스)
    print(unique_words[max_index])