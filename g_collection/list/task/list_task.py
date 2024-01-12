# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

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

while True:
    # 사용자에게 메뉴를 보여주고 선택한 번호를 user_input 에 저장
    user_input = int(input(title + "\n" + menu))
    # 1. 추가하기일 경우
    if user_input == 1:
        # 사용자에게 추가할 상품의 상품명과 가격을 입력받는다.
        append_item, append_price = input(append_message + "\n").split()
        # 가격을 int로 형변환한다.
        append_price = int(append_price)
        # 만약 입력한 상품명이 중복되지 않는다면
        if append_item not in name_list:
            # 상품명 리스트에 넣어준다.
            name_list.append(append_item)
            # 가격 리스트에 가격을 넣어준다.
            price_list.append(append_price)
            # 오류 메시지를 하단에서 출력하지 않기 위해서 즉시 다음 반복으로 continue 해준다.
            continue
        # 만약 중복된 상품명이라면
        else:
            # 에러 메시지에 알맞은 메시지를 담아서 소스코드 하단의 일괄처리로 보낸다.
            result_error_message = append_error_message
    # 2. 수정하기일 경우
    elif user_input == 2:
        # 사용자에게 수정하고 싶은 상품의 상품명을 입력받는다.
        update_item = input(search_name_message_for_update + '\n')
        # 만약 해당 상품이 존재한다면
        if update_item in name_list:
            # 새로운 상품명과 가격을 입력받는다.
            new_name, new_price = input(update_message + "\n").split()
            # 만약 새로 입력한 상품명이 중복되지 않는다면
            if new_name not in name_list:
                # 입력한 새로운 가격을 int로 형변환한다.
                new_price = int(new_price)
                # 해당 상품의 인덱스를 구하여 index 변수에 담는다.
                index = name_list.index(update_item)
                # name_list의 해당 인덱스 원소를 새로운 이름으로 변경한다.
                name_list[index] = new_name
                # price_list의 해당 인덱스 원소를 새로운 가격으로 변경한다.
                price_list[index] = new_price
                # 오류 메시지를 하단에서 출력하지 않기 위해서 즉시 다음 반복으로 continue 해준다.
                continue
            # 만약 새로 입력한 상품명이 이미 존재한다면(중복된 이름이라면)
            else:
                # 에러 메시지에 알맞은 메시지를 담아서 소스코드 하단의 일괄처리로 보낸다.
                result_error_message = update_error_message2
        # 만약 해당 상품이 존재하지 않는다면
        else:
            # 에러 메시지에 알맞은 메시지를 담아서 소스코드 하단의 일괄처리로 보낸다.
            result_error_message = update_error_message
    # 3. 삭제하기일 경우
    elif user_input == 3:
        # 사용자에게 삭제하고 싶은 상품의 상품명을 입력받는다.
        delete_item = input(delete_message + "\n")
        # 만약 해당 상품명이 존재한다면(즉, 삭제 가능하다면)
        if delete_item in name_list:
            # 해당 상품의 인덱스를 구하여 index에 담는다.
            index = name_list.index(delete_item)
            # 가격리스트와 상품명리스트에서 해당 상품을 제거한다.
            del price_list[index]
            del name_list[index]
            # 오류 메시지를 하단에서 출력하지 않기 위해서 즉시 다음 반복으로 continue 해준다.
            continue
        # 만약 해당 상품명이 존재하지 않는다면(즉, 삭제가 불가능하다면)
        # 에러 메시지에 알맞은 메시지를 담아서 소스코드 하단의 일괄처리로 보낸다.
        result_error_message = delete_error_message
    # 4. 검색하기일 경우
    elif user_input == 4:
        # 1. 상품명으로 검색할지, 2. 가격으로 검색할지를 사용자에게 입력받은 후 int로 형변환한다.
        search_option = int(input(search_menu))
        # 상품명으로 검색
        if search_option == 1:
            # 사용자에게 검색할 상품명을 입력받는다.
            search_item = input(search_name_message)
            # 해당 상품명이 존재할 경우
            if search_item in name_list:
                # 해당 상품의 인덱스를 구하여 index에 담는다.
                index = name_list.index(search_item)
                # 해당 인덱스를 통해 상품명과 가격을 search_result에 포매팅하여 담는다.
                search_result = f"*검색 결과\n\t{search_name_message}{search_item}, {search_price_message}{price_list[index]}"
                # 포매팅한 메시지를 출력한다.
                print(search_result)
                # 오류 메시지를 하단에서 출력하지 않기 위해서 즉시 다음 반복으로 continue 해준다.
                continue
            # 해당 상품명이 존재하지 않을 경우
            else:
                # 에러 메시지에 알맞은 메시지를 담아서 소스코드 하단의 일괄처리로 보낸다.
                result_error_message = search_name_error_message
        # 가격으로 검색
        elif search_option == 2:
            # 사용자에게 검색할 가격을 입력받아 int로 형변환한다.
            search_price = int(input(search_price_message))
            # 검색 결과가 여러 개일 수 있으므로 담아놓을 상품명 리스트와 가격 리스트를 선언한다.
            result_name_list = []
            result_price_list = []
            # 오차 범위가 50%이므로 입력한 가격의 0.5배(최솟값)와 1.5배(최댓값)을 구해 변수에 담는다.
            price_start, price_end = search_price * 0.5, search_price * 1.5
            # 가격 리스트의 가격에 대해 반복
            for price in price_list:
                # 해당 가격이 원하는 범위에 들어갈 경우
                if price_start <= price <= price_end:
                    # 범위에 들어가는 해당 가격(검색 결과에 들어갈 가격)의 인덱스를 구해 index에 담는다.
                    index = price_list.index(price)
                    # 검색 결과 상품명 리스트와 가격 리스트에 해당 상품의 정보를 담는다.
                    result_name_list.append(name_list[index])
                    result_price_list.append(price)
            # 검색 결과 리스트의 길이가 1 이상일 경우
            if result_price_list:
                # 검색 결과를 반복문을 통해 출력한다.
                print("*검색결과")
                for i in range(len(result_price_list)):
                    print(f"\t상품명: {result_name_list[i]}, 가격: {result_price_list[i]}")
                # 오류 메시지를 하단에서 출력하지 않기 위해서 즉시 다음 반복으로 continue 해준다.
                continue
            # 검색 결과가 없을 경우
            else:
                # 에러 메시지에 알맞은 메시지를 담아서 소스코드 하단의 일괄처리로 보낸다.
                result_error_message = search_error_message
        # 상품명 검색도 아니고, 가격 검색도 아닌 다른 숫자를 입력할 경우
        else:
            # 에러 메시지에 알맞은 메시지를 담아서 소스코드 하단의 일괄처리로 보낸다.
            result_error_message = "잘못된 번호입니다."
    # 5. 목록보기일 경우
    elif user_input == 5:
        # 상품리스트가 비어있지 않을 경우
        if name_list:
            # 반복문을 통해 상품정보들을 출력한다.
            print("*상품 목록")
            for i in range(len(name_list)):
                print(f"\t상품명: {name_list[i]}, 가격: {price_list[i]}")
            # 오류 메시지를 하단에서 출력하지 않기 위해서 즉시 다음 반복으로 continue 해준다.
            continue
        # 상품리스트가 비어있을 경우
        else:
            # 에러 메시지에 알맞은 메시지를 담아서 소스코드 하단의 일괄처리로 보낸다.
            result_error_message = no_item_message
    # 6. 나가기일 경우
    elif user_input == 6:
        # 알맞은 메시지 출력 후 break을 통해 while문을 탈출한다.
        print("프로그램을 종료합니다.")
        break
    # 1~6이 아닌 잘못된 숫자를 입력할 경우
    else:
        # 에러 메시지에 알맞은 메시지를 담아서 소스코드 하단의 일괄처리로 보낸다.
        result_error_message = "잘못된 번호입니다."
    # continue를 만나지 못하고 도달할 경우 에러 메시지를 출력한다.
    print(result_error_message)
    # 미처 잡지 못한 오류를 방지하기 위해 다음 반복 전에 에러메시지를 다시 초기화한다.
    result_error_message = ""








