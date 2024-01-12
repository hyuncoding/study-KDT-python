# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수

# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.

# 손님
# 이름, 나이, 할인율, 잔액

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print(f"상품명: {self.name}, 가격: {self.price}")

    # __str__() 사용 시
    # def __str__(self):
    #     return f"상품명: {self.name}, 가격: {self.price}"


class Market:
    def __init__(self, product, stock):
        self.product = product
        self.stock = stock

    def sell(self, customer):
        customer.money -= self.product.price * (1 - customer.discount_rate * 0.01)
        self.stock -= 1


class Customer:
    def __init__(self, name, age, discount_rate, money):
        self.name = name
        self.age = age
        self.discount_rate = discount_rate
        self.money = money


product = Product('바나나', 3000)
product.print_info()
market = Market(product, 10)
customer = Customer('한동석', 20, 40, 10000)
market.sell(customer)
print(market.stock)
print(customer.money)




