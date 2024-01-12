# mutable: 변할 수 있는
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
data_list2[0] = 10
print(data_list2)
print(data_list1)

# immutable: 변할 수 없는
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = data_tuple1
# data_tuple2[0] = 10
# test = list(data_tuple2)
# test[0] = 10
# print(test)
data_tuple2 = data_tuple1 + (5, 6)
print(data_tuple2)
print(data_tuple1)

datas = 1, 2
print(type(datas))
print(datas[0])

# 파이썬에는 자바의 final같은 상수 개념이 없으므로
# 튜플의 immutability를 활용하여 1, 등으로 선언한다.
# 상수는 자바처럼 상수명을 대문자로 작성한다.
ERROR_CODE = 1,
print(type(ERROR_CODE))
# 튜플이므로 안의 값을 사용할 때에는 당연히 인덱스로 접근.
print(ERROR_CODE[0])















