import sys

input = sys.stdin.readline

n = int(input())
lis = {'@':'a', '[':'c', '!':'i', ';':'j', '^':'n', '0':'o', '7':'t', '\\':'v','\\\\':'w'}

for x in range(n):
    word = input()
    converted_word = ""
    cnt=0
    for t in word:
        if t in lis.keys():
            t = lis[t]
            cnt+=1
        converted_word += t  # 변환된 문자열에 추가
    if cnt>=len(converted_word):
        print('I don\'t understand')
    else:
        print(converted_word)  # 변환된 문자열 출력
