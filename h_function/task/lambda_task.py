# 'aPPle', 'BananA', 'meLON'을 모두 소문자로 변경
fruits = ['aPPle', 'BananA', 'meLON']
lowered_fruits = list(map(lambda fruit: fruit.lower(), fruits))
print(lowered_fruits)

# 입력받은 한글을 정수로 변경
# 입력 예: 삼오일구
# 출력 예: 3519
hangul = '공일이삼사오육칠팔구'
message = '정수로 변경할 한글 입력: '
user_input = input(message)
result = int("".join(list(map(lambda x: str(hangul.index(x)), user_input))))

print(result)

# 입력받은 정수를 한글로 변경
# 입력 예: 3519
# 출력 예: 삼오일구
message2 = '한글로 변경할 정수 입력: '
user_input2 = input(message2)
result2 = "".join(list(map(lambda x: hangul[int(x)], user_input2)))
print(result2)


# 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
# 위 경로 중 회원 서비스가 아닌 경로만 추출
urls = ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']
# 1. 서비스명(user, post, order)으로 변경(map)
services = list(map(lambda x: x.split('/')[0], urls))
# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)
non_user_services = list(filter(lambda x: x != "user", services))
print(non_user_services)