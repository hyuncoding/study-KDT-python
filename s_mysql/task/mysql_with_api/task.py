from crud_module import *
from message_module import *
import random
from service_module import *


if __name__ == '__main__':
    print(welcome_message)
    while True:
        choice = int(input(option_message))
        # 회원가입
        if choice == 1:
            # 아이디(이메일) 중복검사
            while True:
                email = input(sign_up_email_message).rstrip()
                if not check_email(email):
                    break
                print(email_exist_message)
            password, name = sign_up_after_email_check()
            # SMS API - 랜덤한 인증번호 6자리 발송 후 검사
            while True:
                phone = input(sign_up_phone_message).rstrip()
                verify_code = ""
                for _ in range(6):
                    verify_code += str(random.randint(0, 9))
                try:
                    send_sms(verify_code, phone)
                except Exception as e:
                    print(e)
                    print(phone_error_message)
                    continue
                input_code = input(phone_code_input_message)
                if check_code(verify_code, input_code):
                    print(verify_success_message)
                    break
                else:
                    print(verify_fail_message)
            try:
                sign_up(email, password, name, phone)
                print(sign_up_success_message)
            except Exception as e:
                print(e)
                print(sign_up_fail_message)
        # 로그인
        elif choice == 2:
            # 로그인 후 마이페이지로 이동
            while True:
                email = input(login_email_message).rstrip()
                password = input(login_password_message).rstrip()
                found_member = login(email, password)
                if found_member:
                    print(f"환영합니다. {found_member.get('name')} 님!")
                    break
                else:
                    print(login_error_message)
            # 마이페이지(정보출력)
            for key in found_member:
                if key != "password":
                    print(f"{key}: {found_member[key]}")
            # 비번 변경
            pw_change_option = input(is_password_change_message)
            if pw_change_option in ['Y', 'y']:
                # 회원 비밀번호 변경(EMAIL API) - 랜덤한 코드 10자리 발송 후 검사
                while True:
                    mail_code = ""
                    for _ in range(10):
                        mail_code += str(random.randint(0, 9))
                    print("전송 중...")
                    send_email(mail_code, found_member.get('email'))
                    print(f"\'{found_member.get('email')}\'로 인증번호가 전송되었습니다.")
                    input_code = input(email_code_verify_message).rstrip()
                    if mail_code == input_code:
                        print(verify_success_message)
                        while True:
                            new_password = input(new_password_message).rstrip()
                            try:
                                change_password(found_member.get('email'), new_password)
                                print(password_change_success_message)
                                break
                            except Exception as e:
                                print(e)
                                print(password_change_fail_message)
                        break
                    else:
                        print(verify_fail_message)
        # 나가기
        else:
            break

    # 사용자가 입력한 한국어를 영어로 번역
    # 한국어와 번역된 문장을 DBMS에 저장
    # 번역 내역 전체 조회
    print(trans_welcome_message)
    while True:
        choice = int(input(trans_option_message))
        if choice == 1:
            while True:
                kor_input = input(trans_korean_message).rstrip()
                translated_result = translate(kor_input)
                if translated_result:
                    print(f"번역된 문장은 아래와 같습니다.\n>>> {translated_result}")
                    insert_translated_result(kor_input, translated_result)
                    again_choice = input(trans_again_message).rstrip()
                    if again_choice in ['Y', 'y']:
                        continue
                    else:
                        break
            else:
                print(trans_error_message)
        elif choice == 2:
            found_records = show_translated_records()
            if not found_records:
                print("조회된 내역이 없습니다.")
                continue
            for record in found_records:
                for key in record:
                    print(f"{key}: {record[key]}")

        else:
            break

    # 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)
    # 이미지 경로: https://thumb.mt.co.kr/06/2012/02/2012021613230156226_1.jpg/dims/optimize/
    # 경로와 추출한 텍스트 전체 조회
    print(ocr_welcome_message)
    while True:
        ocr_choice = int(input(ocr_choice_message))
        if ocr_choice == 1:
            # DEBUG FALSE
            # url = input(ocr_input_message).rstrip()
            # DEBUG TRUE
            url = "https://thumb.mt.co.kr/06/2012/02/2012021613230156226_1.jpg/dims/optimize/)"
            result = get_text_with_ocr(url)
            print(f"텍스트 추출 결과: \n{result}")
            insert_image_info(url, result)
        else:
            break
