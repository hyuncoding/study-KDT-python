# 중복이 없고, 순서가 없다.
world_set = {'korea', 'america', 'japan', 'china'}
print(type(world_set))
print(len(world_set))
# print(world_set[1]) -> 순서가 없으므로 가져올 수 없다. 가져오려면 list로 형변환
world_set.add('korea')
print(world_set)

# 중복을 제거할 때 효과적이다.
datas = [1, 1, 3, 2, 3, 4, 1, 4, 4]
print(list(set(datas)))
















