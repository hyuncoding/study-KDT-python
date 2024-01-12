# email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.
message1 = '이메일 입력: '
id, domain = input(message1).split('@')
formatting = f'아이디: {id}\n도메인: {domain}'
print(formatting)

'''
    첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
    각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째자리까지 출력한다.

    1yd: 91.44cm
    1in: 2.54cm

    예)
        yard 입력: 10
        inch 입력: 10

        10 yard는 914.4cm
        10 inch는 25.4cm
'''
message2 = "yard 입력: "
message3 = "inch 입력: "
yard = float(input(message2))
inch = float(input(message3))
yard_to_cm = round(yard * 91.44, 2)
inch_to_cm = round(inch * 2.54, 2)
formatting2 = f'{yard} yard는 {yard_to_cm}cm\n{inch} inch는 {inch_to_cm}cm'
print(formatting2)

