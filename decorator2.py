def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("{} 함수가 호출되기 전 입니다".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display_1():
    print("display_1 함수가 실행되었습니다.")


@decorator_function
def display_2():
    print("display_2 함수가 실행되었습니다.")


# display_1 = decorator_function(display_1)
# display_2 = decorator_function(display_2)
# 위 주석문 둘다 @decorator_function 와 동일

@decorator_function
def display_3(name, age):
    print("display_info({}, {}) 함수가 실행되었습니다.".format(name, age))


display_1()
print()
display_2()
print()
display_3("한승욱", 26)
