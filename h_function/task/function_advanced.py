# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
data_dict = {}

title = "어서와요 과일가게"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

append_error_message = "추가 실패(중복된 상품명)"
update_error_message = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."
result_error_message = ""

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


while True:
    user_input = int(input(title + "\n" + menu))
    # 1. 추가하기
    if user_input == 1:
        append_item, append_price = input(append_message + "\n").split()
        if not select_by_name(append_item):
            insert(name=append_item, price=int(append_price))
            continue
        else:
            result_error_message = append_error_message
    # 2. 수정하기
    elif user_input == 2:
        update_item = input(search_name_message_for_update + '\n')
        if select_by_name(update_item):
            new_name, new_price = input(update_message + "\n").split()
            new_price = int(new_price)
            if not select_by_name(new_name):
                delete(update_item)
                update(name=new_name, price=new_price)
                continue
            else:
                update(name=new_name, price=new_price)
                continue
        else:
            result_error_message = update_error_message
    # 3. 삭제하기
    elif user_input == 3:
        delete_item = input(delete_message + "\n")
        if select_by_name(delete_item):
            delete(delete_item)
            continue
        result_error_message = delete_error_message
    # 4. 검색하기
    elif user_input == 4:
        search_option = int(input(search_menu))
        # 상품명으로 검색
        if search_option == 1:
            search_item = input(search_name_message)
            found_item = select_by_name(search_item)
            if found_item:
                print(f"{found_item['name']}, {found_item['price']}")
                continue
            else:
                result_error_message = search_name_error_message
        # 가격으로 검색
        elif search_option == 2:
            price_input = int(input(search_price_message))

            result = select_by_price(price_input)

            if len(result):
                for product in result:
                    print(f'{product.get("name")}, {product.get("price")}')
                continue

            else:
                result_error_message = search_error_message
        # 상품명 검색도 아니고, 가격 검색도 아닌 다른 숫자를 입력할 경우
        else:
            result_error_message = "잘못된 번호입니다."
    # 5. 목록보기
    elif user_input == 5:
        # 상품 딕셔너리가 비어있지 않을 경우
        if select_all():
            products = select_all()
            for name, price in products.items():
                print(f"{name}, {price}")
            continue
        # 상품 딕셔너리가 비어있을 경우
        else:
            result_error_message = no_item_message
    # 6. 나가기
    elif user_input == 6:
        print("프로그램을 종료합니다.")
        break
    # (cf.) 1~6이 아닌 잘못된 숫자를 입력할 경우
    else:
        result_error_message = "잘못된 번호입니다."
    # continue를 만나지 못하고 도달할 경우 에러 메시지를 출력한다.
    print(result_error_message)
    # 미처 잡지 못한 오류를 방지하기 위해 다음 반복 전에 에러메시지를 다시 초기화한다.
    result_error_message = ""








