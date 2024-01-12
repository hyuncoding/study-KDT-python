# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).

class Member:
    # private: 자신의 클래스에서만 접근 가능
    # 1. 외부에서 접근하지 말자!
    # 2. 외부에서 접근할 때 꼭 메소드로 접근하자!
    __number = 1

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.password = kwargs.get('password')
        self.name = kwargs.get('name')
        self.number = Member.__number
        Member.__number += 1

    @staticmethod
    def get_number():
        return Member.__number

    @classmethod
    def join_as_admin(cls, **kwargs):
        kwargs['id'] = 'admin_' + kwargs.get('id')
        return cls(**kwargs)


member1 = Member(id='hds1234', password='1234', name='한동석')
admin = Member.join_as_admin(id='hgd1234', password='1234', name='홍길동')
print(member1.id)
print(admin.id)


