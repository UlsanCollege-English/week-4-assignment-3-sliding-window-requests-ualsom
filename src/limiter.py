
from collections import deque

class RateLimiter:
    def __init__(self, N, W):
        # TODO: store capacity N, window W, and a queue of timestamps
        self.N = N
        self.W = W
        self._q = None  # TODO

    def allow(self, t):
        """
        Return True if request at time t is allowed (and record it), else False.
        Window is (t - W, t].
        """
        raise NotImplementedError
