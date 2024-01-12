# # 1~15까지 출력
# for i in range(15):
#     print(i+1)
#
# # 30~1까지 출력
# for i in range(30, 0, -1):
#     print(i)
#
# # 1~100까지 중 홀수만 출력
# for i in range(50):
#     print(i * 2 + 1)
#
# # 1~10까지 합 출력
# total = 0
# for i in range(10):
#     total += i + 1
# print(total)
#
# # 1~n까지 합 출력
# n_sum = 0
# message = '자연수 n 입력: '
# n = int(input(message))
# for i in range(n):
#     n_sum += i + 1
# print(n_sum)
#
# # 3 4 5 6 3 4 5 6 3 4 5 6 출력
# for i in range(12):
#     print(i % 4 + 3, end=' ')

# '1,235,500' 를 1235500으로 출력
str_number = '1,235,500'
number = int("".join(str_number.split(',')))
print(number)



