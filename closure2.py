def outer_func():  # 1
    message = "hi"  # 3 프리변수 -> inner_func() 클로저에 저장

    def inner_func():  # 4
        print(message)  # 6

    return inner_func  # 5


my_func = outer_func()

print(my_func)
print()
print(dir(my_func))
print()
print(type(my_func.__closure__))
print()
print(my_func.__closure__)
print()
print(my_func.__closure__[0])
print()
print(dir(my_func.__closure__[0]))
print()
print(my_func.__closure__[0].cell_contents)
print()
