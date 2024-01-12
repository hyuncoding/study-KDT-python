# 캐릭터 닉네임을 정할 때, 비속어를 사용하지 못하게 막아주기
# 바보 멍게 해삼 운영자
# 직접 Error를 제작하여, 발생 시 안내 메세지까지 출력하기

class NickNameError(Exception):
    def __str__(self):
        return "닉네임에 비속어를 사용할 수 없습니다."


def check_nickname(nickname):
    bad_names = ['바보', '멍게', '해삼', '운영자']
    for bad_name in bad_names:
        if bad_name in nickname:
            raise NickNameError


nickname = input('닉네임: ')
try:
    check_nickname(nickname)
    print(f"{nickname}님 환영합니다.")

except NickNameError as e:
    print(e)
