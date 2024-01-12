
# 계좌번호와 전화번호를 중복 검사하는 함수
def check(**kwargs):
    # 계좌번호를 받았을 경우
    if 'account_number' in kwargs:
        value = kwargs.get('account_number')
        for i in range(Bank.total_count):
            for user_info in Bank.banks[i]:
                if user_info.account_number == value:
                    return True
        return False
    # 전화번호를 받았을 경우
    else:
        value = kwargs.get('phone')
        for i in range(Bank.total_count):
            for user_info in Bank.banks[i]:
                if user_info.phone == value:
                    return True
        return False


# 부모 클래스인 Bank
class Bank:
    # 은행 종류의 총 개수
    total_count = 3
    # 은행마다 고객 정보를 담을 2차원 리스트
    banks = [[] for _ in range(total_count)]

    # 생성자: kwargs로 계좌 개설 시 회원의 정보들을 받는다.
    def __init__(self, **kwargs):
        self.owner = kwargs['owner']
        self.account_number = kwargs['account_number']
        self.phone = kwargs['phone']
        self.password = kwargs['password']
        self.money = 0
        # 어떤 은행인지는 필드로 굳이 담아놓지 않는다.
        bank_choice = kwargs['bank_choice']
        # banks 2차원 리스트의 각 은행 고객정보 리스트에는 나중에 접근이 용이하도록
        # self, 즉 주소값을 담는다. 딕셔너리 대신.
        # 물론 딕셔너리를 담을 경우 __dict__를 사용하여 banks에 담고,
        # dict['object'] = self 의 형식으로 self 주소값을 저장하여
        # 나중에 필요할 경우 접근하여 사용할 수 있도록 할 수도 있다.
        Bank.banks[bank_choice - 1].append(self)


    # 클래스메소드로 어떤 은행의 생성자를 호출할지 결정
    # 선택한 은행이 무엇인지는 kwargs에서 같이 받는다.
    # return cls(**kwargs)의 cls 자리에 적절한 자식 클래스의 생성자를 작성해준다.
    @classmethod
    def open_account(cls, **kwargs):
        bank_choice = kwargs['bank_choice']
        if bank_choice == 1:
            return ShinHan(**kwargs)
        elif bank_choice == 2:
            return KookMin(**kwargs)
        return KaKao(**kwargs)

    # 계좌번호 중복검사
    @staticmethod
    def check_account_number(account_number):
        return check(account_number=account_number)

    # 전화번호 중복검사
    @staticmethod
    def check_phone(phone):
        return check(phone=phone)

    # 입금하기
    def deposit(self, amount):
        self.money += amount

    # 출금하기
    def withdraw(self, amount):
        self.money -= amount

    # 잔액 조회
    def balance(self):
        return self.money

    # __str__() 재정의하여 print()로 객체 호출 시 정보 출력
    def __str__(self):
        return f'예금주: {self.owner}\n'\
                f'계좌번호: {self.account_number}\n'\
                f'핸드폰번호: {self.phone}\n'\
                f'비밀번호: {self.password}\n'\
                f'통장잔고: {self.money}'

    # 로그인하기 기능(입/출금 시 우선 사용)
    @staticmethod
    def login(**kwargs):
        bank_choice = kwargs['bank_choice']
        account_number = kwargs['account_number']
        password = kwargs['password']
        # 일치하는 정보가 있을 경우(해당 은행에 대해서만) 회원 객체를 return
        # 없을 경우 None
        for user_info in Bank.banks[bank_choice - 1]:
            if user_info.account_number == account_number and \
                    user_info.password == password:
                return user_info
        return None

    # 전화번호와 비밀번호로 유저 정보 찾기
    @staticmethod
    def find_account_by_phone(bank_choice, phone, password):
        for user_info in Bank.banks[bank_choice - 1]:
            if user_info.phone == phone and user_info.password == password:
                return user_info
        return None

    # 찾아낸 회원 객체에 대하여 새로운 계좌번호로 업데이트하고,
    # 이때 새로운 계좌번호가 중복될 경우 False를 return하고 업데이트는 수행하지 않는다.
    # 반대로 중복되지 않을 경우 업데이트를 수행하고 True를 return한다.
    @staticmethod
    def update_account_number(user_info, new_account_number):
        if check(account_number=new_account_number):
            return False
        user_info['account_number'] = new_account_number
        return True


class ShinHan(Bank):
    # 입금 시 수수료 50%
    def deposit(self, amount):
        amount = int(amount * 0.5)
        super().deposit(amount)


class KookMin(Bank):
    # 출금 시 수수료 50%
    def withdraw(self, amount):
        amount = int(amount * 1.5)
        super().withdraw(amount)


class KaKao(Bank):
    # 잔액 조회 시 반토막
    def balance(self):
        self.money //= 2
        return super().balance()


if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 계좌번호 찾기\n"\
           "6. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    new_account_number_message = "새로운 계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"
    account_exist_message = "중복된 계좌번호입니다."
    phone_exist_message = "중복된 전화번호입니다."
    update_account_result_message = "변경되었습니다."


    while True:
        # 은행 메뉴
        bank_choice = int(input(bank_menu))
        if bank_choice == 4:
            break

        if bank_choice < 1 or bank_choice > len(Bank.banks):
            continue

        while True:
            # 서비스 메뉴
            service = int(input(menu))
            # 계좌 개설
            if service == 1:
                owner = input(owner_message)
                # 계좌번호가 중복되지 않을 때까지 반복해서 입력 받기
                while True:
                    account_number = input(account_number_message)
                    if not check(account_number=account_number):
                        break
                # 전화번호도 마찬가지
                while True:
                    phone = input(phone_message)
                    if not check(phone=phone):
                        break
                # 비밀번호는 길이가 반드시 4여야 하므로 조건 만족할 때까지 반복
                while True:
                    password = input(password_message)
                    if len(password) == 4:
                        break
                # classmethod로 만든 객체화 메소드 호출
                Bank.open_account(bank_choice=bank_choice,
                                  owner=owner,
                                  account_number=account_number,
                                  phone=phone,
                                  password=password)
                # 바로 로그인하여 계좌정보 출력
                user_info = Bank.login(bank_choice=bank_choice, account_number=account_number, password=password)
                print(user_info)
            # 입금
            elif service == 2:
                account_number = input(account_number_message)
                password = input(password_message)
                # 로그인해서 회원정보 가져오기
                user_info = Bank.login(bank_choice=bank_choice, account_number=account_number, password=password)
                if user_info is None:
                    print(error_message)
                    continue
                # 처음에 고른 은행과, 회원이 속한 은행이 다를 경우 에러 메시지 출력
                # 즉, 회원 객체가 처음에 고른 은행의 인스턴스 variable이어야 한다.(isinstance()사용)
                if not isinstance(user_info, [ShinHan, KookMin, KaKao][bank_choice-1]):
                    print(error_message)
                    continue
                # 다 확인되면 이제 입금액을 입력받고 입금 수행
                deposit_amount = int(input(deposit_message))
                user_info.deposit(deposit_amount)
            # 출금
            elif service == 3:
                account_number = input(account_number_message)
                password = input(password_message)
                user_info = Bank.login(bank_choice=bank_choice, account_number=account_number, password=password)
                if user_info is None:
                    print(error_message)
                    continue
                withdraw_amount = int(input(withdraw_message))
                # 은행이 국민은행일 경우 출금 수수료를 포함한 총액이 통장에 있어야 하므로 검사( 3항 연산자 사용 )
                # 다른 은행일 경우 수수료는 0, 그냥 출금 희망액이 통장에 있는지 검사
                if withdraw_amount * (1.5 if bank_choice == 2 else 1) <= user_info.money:
                    user_info.withdraw(withdraw_amount)
                # 잔액 부족 시 에러 메시지
                else:
                    print(error_message)
            # 잔액 확인하기
            elif service == 4:
                account_number = input(account_number_message)
                password = input(password_message)
                user_info = Bank.login(bank_choice=bank_choice, account_number=account_number, password=password)
                if user_info is None:
                    print(error_message)
                    continue
                print(f"잔액: {user_info.balance()}원")
            # 계좌번호 재설정
            elif service == 5:
                phone = input(phone_message)
                password = input(password_message)
                user_info = Bank.find_account_by_phone(bank_choice, phone, password)
                if user_info is None:
                    print("전화번호 혹은 비밀번호가 잘못되었습니다.")
                    continue
                # 새로운 계좌번호가 중복되지 않도록 반복하여 입력
                while True:
                    new_account_number = input(new_account_number_message)
                    if Bank.update_account_number(user_info, new_account_number):
                        print(update_account_result_message)
                        break
                    print(account_exist_message)
            else:
                break


