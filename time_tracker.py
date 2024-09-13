import pytz
from datetime import datetime

class TimeTracker:

    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0

    def start(self):
        self.start_time = datetime.now()
        print(f'활동 시작 시간: {self.start_time}')

    def stop(self):
        if self.start_time is None:
            print('시작 시간이 설정되지 않았습니다. 먼저 start 메서드를 호출하세요.')
        else:
            self.end_time = datetime.now()
            self.elapsed_time = (self.end_time - self.start_time).seconds / 60  # 초 말고 분으로 출력하는 방법 찾아야함
            print(f'활동 종료 시간: {self.end_time}')
            print(f'총 경과 시간: {self.elapsed_time}')

    def get_elapsed_time(self):
        if self.start_time and self.end_time:
            return self.elapsed_time
        else:
            print('아직 활동이 종료되지 않았거나 시작되지 않았습니다.')
            return 0


if __name__ == "__main__":
    tracker = TimeTracker()
    tracker.start()

    # 여기서 실제로 시간을 지연시키려면 time.sleep()을 사용할 수 있지만, 코드 실행을 바로 확인하기 위해 주석 처리함
    import time

    time.sleep(61)  # 61초 대기

    tracker.stop()
    print(f"공부한 시간: {tracker.get_elapsed_time()} 분")