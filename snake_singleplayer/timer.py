import time


class Timer:
    def __init__(self, second: float, end_timer: float):
        self.start_time = time.time()
        self.second = second
        self.end_timer = end_timer
        self.previous_sec = 0
        self.elapsed_time = None

    def compare_time(self) -> bool:
        self.elapsed_time = time.time() - self.start_time
        if self.elapsed_time >= self.previous_sec:
            self.previous_sec += self.second
            if float(self.previous_sec) == float(self.end_timer):
                return True
        return False
