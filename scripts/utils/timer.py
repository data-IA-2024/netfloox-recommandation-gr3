import time
import datetime

class Timer:

    def __init__(self, now=False):
        self._start = time.time()
        if now : print('Started at : ', datetime.datetime.now())
    
    def elapsed(self):
        delta = round(time.time()-self._start)
        return str(datetime.timedelta(seconds=delta))