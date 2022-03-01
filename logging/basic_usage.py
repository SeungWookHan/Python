# logging 모듈은 파이썬 자체에 내장되어 있는 모듈
# 여러 이벤트를 추적함으로써 어떤 이벤트가 발생하였고 이에 대해 어떤 해결책을 강구해야 할지 판단
import logging

# 생성
logger = logging.getLogger("myloger")
  # 아무것도 입력하지 않으면 root logger 생성됨

# 레벨 부여
logger.setLevel(logging.INFO)
'''
DEBUG - 간단히 문제를 진단하고 싶을 때 필요한 자세한 정보 기록
INFO - 계획대로 작동하고 있음을 알리는 확인용
WARNING - 작동은 하지만, 예상치 못한 일이 일어났거나 일어날 것으로 예측된다는 것을 알림
ERROR - 중대한 문제로 소프트웨어가 몇몇 기능을 수행하지 못함을 알림
CRITICAL - 작동이 불가능한 수준의 심각한 에러가 발생함
'''
  # 여기서 위 level을 소문자로 바꾸어 메서드로 사용하면 메시지 출력 가능
logger.info("Test Message")

# handler / formatter 설정
'''
handler의 종류는 15개.
이 중 대표적인 것이 
StreamHandler - 콘솔에 메시지 전달
FileHandler - File에 메시지 전달
'''
logging.Formatter(
  fmt = None, # 메시지 출력 형태, None이면 raw 메시지 출력
  datefmt = None, # 날짜 출력 형태, None이면 %Y-%m-%d %H:%M:%S
  style = '%' # %, {, $ 중 하나. fmt의 스타일 결정
)

  # handler 객체 생성
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename="test.log")
  
  # formatter 객체 생성
formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

  # handler 레벨 설정
stream_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

  # handler에 format 적용
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# logger에 생성한 handler 추가
logger.addHandler(stream_handler)
logger.addHandler(file_handler)