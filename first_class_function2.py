def logger(msg):
    def log_message():
        print("Log:" + msg)
    return log_message


log_hi = logger("hi")

print(log_hi)
log_hi()

print(logger)
del logger

try:
    print(logger)
except NameError:
    print('NameError: logger는 존재하지 않습니다.')

log_hi()  # logger가 지워진 뒤에도 Log: Hi"가 출력됩니다.
