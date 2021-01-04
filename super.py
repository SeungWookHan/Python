class Dog:
    def __init__(self):
        print("woof woof")

    def pee(self):
        print("I will pee")


class Puppy(Dog):
    def pee(self):
        print("go to the part")


p = Puppy()
p.pee()


# woof woof
# go to the part 가 노출된다.
# 하지만 우리는 부모 클래스의 I will pee도 같이 노출시켜주고자 한다.
# 여기서 super() 개념이 필요한 것이다


class Puppy2(Dog):
    def pee(self):
        print("go to the park")
        super().pee()


p2 = Puppy2()
p2.pee()