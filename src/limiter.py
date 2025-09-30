from collections import deque

class RateLimiter:
    def __init__(self, N, W):
        self.N = N        # max number of requests
        self.W = W        # time window size
        self._q = deque() # queue to store timestamps

    def allow(self, t):
        # Remove timestamps outside the window (older than t - W)
        while self._q and self._q[0] <= t - self.W:
            self._q.popleft()

        if len(self._q) < self.N:
            self._q.append(t)
            return True
        else:
            return False
