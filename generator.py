# 이터레이터를 생성해주는 함수, 함수안에 yield 키워드 사용

def test_generator():
  yield 1
  yield 2
  yield 3
  
gen = test_generator()
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))

'''
<class 'generator'>
1
2
3
Traceback (most recent call last):
  File "/Users/wooogy-dev/dev/Python/generator.py", line 13, in <module>
    print(next(gen))
StopIteration
'''

import collections
print(isinstance(gen, collections.Iterator)) # True


def three_generator():
  a = [1, 2, 3]
  for i in a:
    yield i

gen2 = three_generator()
print(list(gen2)) # [1, 2, 3]

# 이러한 상황에서 for문 대신 yield from 사용 가능
def three_generator_():
  a = [1, 2, 3]
  yield from a

gen2_ = three_generator_()
print(list(gen2_)) # [1, 2, 3]