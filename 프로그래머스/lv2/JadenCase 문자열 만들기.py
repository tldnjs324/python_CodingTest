def solution(s):
    words = s.split(' ') # 단어를 공백 기준으로 나누기
    for i in range(len(words)):
        words[i] = words[i].capitalize() # 첫 문자만 대문자로, 나머지 소문자로 바꿔줌

    answer = ' '.join(words) # 공백을 다시 단어로 묶어줌
    return answer