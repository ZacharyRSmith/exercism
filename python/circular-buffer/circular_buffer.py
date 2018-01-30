class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self._set_init_state()

    def clear(self):
        self._set_init_state()

    def overwrite(self, item):
        pass

    def read(self):
        res = self._buffer[self._oldest_idx]
        if res is None:
            raise BufferEmptyException(f'Cannot read: buffer is empty.')
        self._buffer[self._oldest_idx] = None
        self._oldest_idx = self._incr_idx(self._oldest_idx)
        return res

    def write(self, item):
        if self._buffer[self._next_idx] is not None:
            raise BufferFullException(f'Cannot write: buffer is full.')
        self._buffer[self._next_idx] = item
        self._next_idx = self._incr_idx(self._next_idx)

    def _incr_idx(self, idx):
        next_idx = idx + 1
        return next_idx if next_idx < len(self._buffer) else 0

    def _set_init_state(self):
        self._buffer = [None for i in range(self.capacity)]
        self._oldest_idx = 0
        self._next_idx = 0
