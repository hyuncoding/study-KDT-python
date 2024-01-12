from market_module import *
from message_module import *

if __name__ == '__main__':
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