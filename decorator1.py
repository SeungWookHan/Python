def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def display():
    print("디스플레이 함수가 실행되었습니다.")


decorator_display = decorator_function(display)
decorator_display()
