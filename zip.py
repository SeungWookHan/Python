# 리스트 [1, 2, 3, 4]가 있을때 2개씩 묶어주기
# (1, 2), (2, 3), (3, 4)
lst = [1, 2, 3, 4]
print(lst[1:]) # [2, 3, 4]
print(lst[:-1]) # [1, 2, 3]

print(list(zip(lst[:-1], lst[1:]))) # [(1, 2), (2, 3), (3, 4)]

for a, b in zip(lst[:-1], lst[1:]):
  print(a, b)
  """
  1 2
  2 3
  3 4
  """