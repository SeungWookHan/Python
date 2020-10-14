# outer_func 함수 하나로 h1태그와 p태그로 문자열을 감싸는 함수 만들기
# text를 inner_func의 매개인자로
def outer_func(tag):
    # text = "some text"
    tag = tag

    def inner_func(text):
        text = text
        print("<{0}>{1}<{0}>".format(tag, text))
    return inner_func


h1_func = outer_func("h1")
p_func = outer_func("p")

h1_func("h1태그의 안입니다.")
p_func("p태그의 안입니다.")
