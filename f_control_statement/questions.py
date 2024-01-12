# if문 문제

'''

길동이는 2024년 윤년을 맞이한 기념으로,
사용자가 연도를 입력하면 윤년인지 아닌지를 판별해주는 프로그램을 만들고자 한다.
길동이를 도와 해당 프로그램을 만들어보자.

참고: 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 혹은 400의 배수일 때이다.

입력: 연도가 주어진다.

출력: 입력한 연도가 윤년이면 1, 윤년이 아니면 0을 출력한다.

'''

message = '연도 입력: '
example_message = "ex) 2024"
year = int(input(message + '\n' + example_message + '\n'))
result = 0
if not year % 4:
    if year % 100 or not year % 400:
        result = 1
print(result)

# for문 문제

'''

정수 n을 입력받은 후, 아래 예제 출력과 같이 구구단을 출력하는 프로그램을 작성하시오.

예제 입력:

정수 입력: 2

예제 출력: 

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18

'''

message = '정수 입력: '
n = int(input(message))
for i in range(9):
    print(f"{n} * {i+1} = {n * (i+1)}")


# while문 문제

'''

두 정수가 입력되면 두 정수의 합을 출력하는 프로그램을 작성하시오.
두 정수는 공백으로 구분되어 있으며, 입력은 여러 줄이다.
입력의 마지막에는 0 0이 입력되며 이때에는 아무 것도 출력하지 않고 프로그램이 종료되도록 한다.

'''

number1, number2 = 0, 0
while True:
    number1, number2 = map(int, input().split())
    if not number1 and not number2:
        break
    print(number1 + number2)

