import time


class Timer:
    def __init__(self):
        self._elapsed = 0

    def __enter__(self):
        self._start = time.process_time()

    def __exit__(self, err_type, err_value, traceback):
        self._end = time.process_time()
        self._elapsed = self._end - self._start

    @property
    def elapsed(self):
        return self._elapsed
