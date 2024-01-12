# fish.txt
# 사용자에게 입력받은 물고기를 fish.txt에 작성한다.
# 사용자가 q를 입력하면, fish.txt의 전체 내용을 삭제한다.
# 사용자가 r을 입력하면, fish.txt의 전체 내용을 콘솔에 출력한다.
# with open('fish.txt', 'w', encoding='utf-8') as file:
#     pass


# with open('fish.txt', 'a', encoding='utf-8') as file:
#     fish = input('물고기를 입력하세요: ')
#     file.write(fish + '\n')
#
#
# def get_order(order):
#     if order == 'q':
#         with open('fish.txt', 'w', encoding='utf-8') as file:
#             file.write('')
#     elif order == 'r':
#         try:
#             with open('fish.txt', 'r', encoding='utf-8') as file:
#                 line = None
#                 while line != '':
#                     line = file.readline()
#                     print(line, end="")
#         except FileNotFoundError as e:
#             print(e)
#             print('파일이 존재하지 않습니다.')
#
#
# order = input('입력한 내용을 삭제하시려면 q를, 전체 조회를 하시려면 r을 입력해주세요: ')
# get_order(order)

# title = 'q: 삭제하기, r: 읽기'
# message = '물고기: '
#
# while True:
#     path = input('경로: ')
#     user_input = input(title + '\n' + message)
#
#     if input == 'q':
#         with open(path, 'w', encoding='utf-8') as file:
#             pass
#
#     elif input == 'r':
#         try:
#             with open(path, 'r', encoding='utf-8') as file:
#                 line = None
#                 while line != '':
#                     line = file.readline()
#                     print(line, end="")
#             break
#         except FileNotFoundError as e:
#             print(e)
#             print('파일이 존재하지 않습니다.')
#     else:
#         with open(path, 'a', encoding='utf-8') as file:
#             fish = input('물고기를 입력하세요: ')
#             file.write(fish + '\n')

# 고등어를 참치로 수정하기

content = ''
with open('fish.txt', 'r', encoding='utf-8') as file:
    line = None
    while line != '':
        line = file.readline()
        if line == '고등어\n':
            content += '참치\n'
            continue
        content += line
    # print(f'content: {content}')

with open('fish.txt', 'w', encoding='utf-8') as file:
    file.write(content)

with open('fish.txt', 'r', encoding='utf-8') as file:
    print("".join(file.readlines()))






