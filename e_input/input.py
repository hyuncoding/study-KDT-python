# 문자열끼리만 연결(+)이 가능하다!
# data = 3
# print('안' + str(data))

# name = input("이름: ")
# print(f'{name}님 환영합니다.')

# 제 이름은 ???, 키는 ???cm입니다.
# name = input("이름: ")
# height = input("키: ")
# formatting = f'제 이름은 {name}, 키는 {height}cm입니다.'
# print(formatting)

# 두 정수를 입력받은 후 곱셈 결과 출력
number1 = int(input("첫 번째 정수 입력: "))
number2 = int(input("두 번째 정수 입력: "))
result = number1 * number2
formatting1 = f'{number1} x {number2} = {result}'
print(formatting1)

# message1 = '첫 번째 정수: '
# message2 = '두 번째 정수: '
# number1 = int(input(message1))
# number2 = int(input(message2))
# result = number1 * number2
# formatting = f'{number1} * {number2} = {result}'
# print(formatting)

# map(각각 어떻게 바꿀 것인가, [](이터러블 객체))
# message = '두 정수를 입력하세요.'
# example_message = '예)1, 3'
# number1, number2 = map(int, input(message + "\n" + example_message + "\n").split(', '))
# result = number1 * number2
# formatting = f'{number1} * {number2} = {result}'
#
# print(formatting)

# 현재 시간을 입력하고 시와 분으로 분리하여 출력
message1 = '현재 시간을 입력하세요.'
example_message1 = '예)11:30'
hour, minute = input(message1 + '\n' + example_message1 + '\n').split(':')
formatting1 = f'현재 시간은 {hour}시 {minute}분입니다.'
print(formatting1)

# 핸드폰 번호를 -과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
message2 = '핸드폰 번호를 입력하세요.'
example_message2 = '예)010-1234-1234'
front, middle, end = input(message2 + '\n' + example_message2 + '\n').split('-')
formatting2 = f'입력하신 번호의 앞자리는 {front}, 중간은 {middle}, 마지막은 {end}입니다.'
print(formatting2)

# 이름과 나이를 한 번에 입력받은 뒤 "000님의 나이는 000살" 형식으로 출력
message3 = '이름과 나이를 입력하세요.'
example_message3 = '예)홍길동, 20'
name, age = input(message3 + '\n' + example_message3 + '\n').split(', ')
formatting3 = f'{name}님의 나이는 {age}살'
print(formatting3)

# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
message4 = '세 개의 정수를 입력하세요.'
example_message4 = 'ex)1, 5, 10'
number1, number2, number3 = map(int, input(message4 + '\n' + example_message4 + '\n').split(', '))
result = number1 + number2 + number3
formatting4 = f'{number1} + {number2} + {number3} = {result}'
print(formatting4)






