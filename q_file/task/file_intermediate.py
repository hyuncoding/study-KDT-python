# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""


with open('alice.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()

temp = []
for character in content:
    if 'a' <= character <= 'z':
        temp.append(character)
    else:
        temp.append(" ")
content = "".join(temp)

count_dict = dict()
for word in content.split():
    if len(word) >= 2:
        if not count_dict.get(word):
            count_dict[word] = 1
        else:
            count_dict[word] += 1

result_list = []
for word, cnt in count_dict.items():
    if cnt >= 100:
        result_list.append((word, cnt))

result_list.sort(key=lambda x: x[1], reverse=True)
for word, cnt in result_list:
    print(word, cnt)


