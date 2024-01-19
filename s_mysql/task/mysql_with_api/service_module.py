import json
from s_mysql.task.mysql_with_api.sms import message
from message_module import *
from crud_module import *
import hashlib
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib.request
import requests


def check_email(email):
    query = "select email, password, name, phone from tbl_member where email = %s"
    params = (email,)
    found_member = find_by_id(query, params)
    if found_member:
        return True
    return False


def sign_up_after_email_check():
    password = input(sign_up_password_message)
    encryption = hashlib.sha256()
    encryption.update(password.encode('utf-8'))
    password = encryption.hexdigest()
    name = input(sign_up_name_message)
    return password, name


def sign_up(email, password, name, phone):
    query = "insert into tbl_member (email, password, name, phone) \
             values (%s, %s, %s, %s)"
    params = (email, password, name, phone)
    save(query, params)


def send_sms(code: str, phone: str):
    data = {
            'messages': [
                {
                    'to': phone,
                    'from': '01050119661',
                    'text': f"인증번호는 [{code}] 입니다."
                }
            ]
        }
    res = message.send_many(data)


def check_code(code: str, input_code: str):
    if code == input_code:
        return True
    return False


def login(email: str, password: str):
    encryption = hashlib.sha256()
    encryption.update(password.encode('utf-8'))
    password = encryption.hexdigest()
    query = "select email, password, name, phone from tbl_member where email = %s and password = %s"
    params = (email, password)
    found_member = find_by_id(query, params)
    return found_member


def send_email(content: str, email: str):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "hyunstwolte@gmail.com"
    receiver_email = email
    email_password = "qvrh dffv wslj vqqt"
    content = f"<h1>인증번호는 [{content}] 입니다.\n정확하게 입력해주세요.</h1>"

    msg = MIMEText(content, 'html')
    data = MIMEMultipart()
    data.attach(msg)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, data.as_string())


def change_password(email: str, new_password: str):
    encryption = hashlib.sha256()
    encryption.update(new_password.encode('utf-8'))
    new_password = encryption.hexdigest()
    query = "update tbl_member set password = %s where email = %s"
    params = (new_password, email)
    update(query, params)


def translate(kor: str):
    client_id = "bY0GZUJf9OBTd0DDPY1m"
    client_secret = "PvocgOIXSA"
    encoding_text = urllib.parse.quote(kor)
    data = f"source=ko&target=en&text={encoding_text}"
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)

    # -H
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response = json.loads(response.read().decode("utf-8"))
        return response['message']['result']['translatedText']

    return None


def insert_translated_result(original_message: str, translated_message: str):
    query = ("insert into tbl_translation (original_message, translated_message) \
              values (%s, %s)")
    params = (original_message, translated_message)
    save(query, params)


def show_translated_records():
    query = "select * from tbl_translation"
    return find_all(query)


def get_text_with_ocr(url):
    url = 'https://api.ocr.space/parse/imageurl?apikey=K86291994088957&url=' + \
          url + '&language=kor&isOverlayRequired=true'

    response = requests.get(url)
    response.raise_for_status()

    result = response.json()
    return result['ParsedResults'][0]['ParsedText']

def insert_image_info(image_url, image_text):
    query = "insert into tbl_image (image_name, image_text) \
              values (%s, %s)"
    params = (image_url, image_text)
    save(query, params)


def show_all_translate_records():
    query = "select id, image_name, image_text from tbl_image"
    return find_all(query)