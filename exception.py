

class TimeoutException(BaseException):
    txt = """ Timedout Please Increase Your Timeout"""

    def __str__(self) -> str:
        return self.txt
