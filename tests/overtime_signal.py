
# Signal
import signal


TIMEOUT = 8


# TimeOutException
class TimeOutException(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeOutException("Database Error!")


signal.signal(signal.SIGTERM, timeout_handler)
