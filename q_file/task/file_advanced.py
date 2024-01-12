from advanced.calc import Calculator

menu = "1. 계산하기\n2. 로그보기\n3. 종료하기\n"
number_message = "두 정수를 입력하세요.\n예) 3 4\n"
oper_message = "연산자를 입력하세요.(+, -, &, / 중 1 택)\n"
error_message = "다시 시도하세요."
error_code = None

while True:
    choice = int(input(menu))
    # 계산하기
    if choice == 1:
        error_code = ""
        number1, number2, oper = "", "", ""
        try:
            number1, number2 = map(int, input(number_message).split())
            oper = input(oper_message)

        except ValueError:
            error_code = "ValueError"

        finally:
            if oper == "/":
                if number2 == 0:
                    error_code = "ZeroDivisionError"
            result = Calculator(number1).calc(number2, oper, error_code=error_code)
            if result:
                print(result)
            else:
                print("다시 시도해주세요.")
    # 로그보기
    elif choice == 2:
        try:
            with open('log.txt', 'r', encoding='utf-8') as file:
                print(file.read())
        except FileNotFoundError:
            print('파일이 존재하지 않습니다.')
    elif choice == 3:
        pass

    else:
        print(error_message)