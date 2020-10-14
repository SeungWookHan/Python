def outer_func():  # 1
    message = "hi"  # 3 프리변수 -> inner_func() 클로저에 저장

    def inner_func():  # 4
        print(message)  # 6  

    return inner_func  # 5
    # return에 () 있을때와 없을때 다름
    # outer_func이 리턴할때 inner_func 함수를 실행하지않고, 함수 오브젝트를 리턴


# outer_func()  # 2
my_func = outer_func()  # 2 리턴값이 inner_func를 변수에 할당

my_func()
my_func()
my_func()

print(my_func()) # 이렇게 하면 hi, none이 같이 노출됨. my_func()자체는 None형