class RecentCounter:
    def __init__(self):
        self.counter = []
        self.start = 0
    def ping(self, t: int) -> int:
        self.counter.append(t)
        while self.counter[self.start] < t - 3000:
            self.start += 1
        return len(self.counter) - self.start