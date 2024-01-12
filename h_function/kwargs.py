# keyword arguments

# def introduce(**intro):
#     print(type(intro))
#     print(f'name: {intro["name"]}')
#
#
# introduce(name='한동석')
# introduce(**{'name': '한동석'})
# info_dict = {'name': '한동석'}
# introduce(**info_dict)

# # 주문 총 가격과 주문한 회원의 정보 출력
# def order_info(*args, **kwargs):
#     total = 0
#     for i in args:
#         total += i
# 
#     print(f'{kwargs["name"]}님의 총 주문 가격: {total}원')
# 
# order_info(3000, 2000, 1000, name='한동석')


# 국어, 영어, 수학 점수의 평균 구하기
# kwargs를 사용
# def get_average(**kwargs):
#     kor = kwargs['kor']
#     eng = kwargs['eng']
#     math = kwargs['math']
#     return (kor + eng + math) / 3
#
# print(get_average(kor=100, eng=40, math=50))

# 국어, 영어, 수학 점수의 평균 구하기
# 사용자가 원하는 자리수에서 반올림해준다.
# 자리수를 받지 않았다면, 기본값을 리턴한다.
# def get_average_and_round(**kwargs):
#     kor = kwargs['kor']
#     eng = kwargs['eng']
#     math = kwargs['math']
#     average = (kor + eng + math) / 3
#     if 'round' in kwargs:
#         average = round(average, kwargs['round'])
#     return average
#
# print(get_average_and_round(kor=100, eng=40, math=50))
# print(get_average_and_round(kor=100, eng=40, math=50, round=3))


# 반드시 key와 함께 사용하고자 할 때에는 매개변수의 시작을 *로 선언한다.
# def get_average(*, kor, eng, math):
#     return (kor + eng + math) / 3
# 
# print(get_average(kor=100, eng=40, math=50))


# 주문 총 가격과 주문한 회원의 정보 출력
def order_info(*args, **kwargs):
    '''
    주문 총 가격과 주문한 회원의 정보 출력
    :param args: 주문 가격들 
    :param kwargs: 회원의 정보
    '''
    total = 0
    for i in args:
        total += i

    print(f'{kwargs["name"]}님의 총 주문 가격: {total}원')

order_info(3000, 2000, 1000, name='한동석')


help(order_info)