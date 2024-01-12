# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.
# 쿠폰 종류는 단 1개, 쿠폰 할인율은 40과 같은 1~100사이의 정수
## 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2

# 출력 예시1
# [1000, 2000]

# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100


# 출력 예시2
# [700, 2800, 3500]


# coupon=40
# count=5
#
# 아래와 같이 무조건 1개 종류의 쿠폰 여러 장이다.
# 40%쿠폰 5개
#
# 아래와 같은 상황은 없다.
# 10%쿠폰 1개, 20%쿠폰 2개

def get_total(*args, **kwargs):
    '''

    :param args: 주문 금액(pay)들을 받는다.
    :param kwargs: coupon=할인율(백분율, 1~100 사이의 정수), count=개수 형식의 딕셔너리이다.
    :return: 할인율이 적용된 각 주문 금액의 최종 결제 금액을 리스트에 담아 return한다.
    '''
    
    # 할인율을 kwargs 딕셔너리에서 'coupon' 키값으로 가져와 discount_rate 변수에 담기
    discount_rate = kwargs['coupon']
    # 쿠폰의 개수를 kwargs 딕셔너리에서 'count' 키값으로 가져와 count 변수에 담기
    count = kwargs['count']
    # comprehension 사용
    # 쿠폰의 개수보다 현재 반복 i(주문 상품의 인덱스)가 작으면 쿠폰 사용 가능
    # 쿠폰의 개수보다 i가 크거나 같을 경우 쿠폰 사용이 불가능하므로 할인적용 불가
    return [args[i] * (100 - discount_rate) // 100 for i in range(len(args)) if i < count]

print(get_total(1000, 4000, 5000, coupon=30, count=2))


def use_coupon(*pay, **kwargs):
    '''

    :param pay: 주문 금액들
    :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액들
    '''
    if 'coupon' in kwargs:
        return [
            pay[i] * (100 - kwargs.get('coupon')) // 100
            for i in
            range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
        ]

    return None

help(use_coupon)
result = use_coupon(1000, 2000, 3000, coupon=50, count=2)

if result:
    print(result)
else:
    print('쿠폰이 없습니다.')
