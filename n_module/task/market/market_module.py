from connection_module import data_dict

# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.


# 추가하기
def insert(**kwargs):
    '''

    :param kwargs: {'name': '상품명', 'price': 가격}
    '''
    name, price = kwargs.values()
    data_dict[name] = price


# 삭제하기
def delete(name):
    del data_dict[name]


# 수정하기
def update(**kwargs):
    '''

    :param kwargs: {'name': '새로운 상품명', 'price': 새로운 가격}
    '''
    name, price = kwargs.values()
    data_dict[name] = price


# 상품명으로 검색
def select_by_name(keyword):
    result = {}
    if keyword in data_dict:
        result = {'name': keyword, 'price': data_dict[keyword]}
    return result

# 가격으로 검색
def select_by_price(price, range=50):
    result = []
    min = price * range * 0.01
    max = price * (100 + range) * 0.01

    for name, price in data_dict.items():
        if min <= price <= max:
            result.append({'name': name, 'price': price})

    return result


# 목록보기
def select_all():
    return data_dict