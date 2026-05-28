# File: app/services/id_generator.py

import string
import time
import threading

class Base62Encoder:
    chars = string.ascii_letters + string.digits

    def encode(self, num: int) -> str:
        if num == 0:
            return self.chars[0]
        base = len(self.chars)
        result = []
        while num > 0:
            result.append(self.chars[num % base])
            num //= base
        return ''.join(reversed(result))

class IDGenerator:
    def __init__(self):
        self.lock = threading.Lock()
        self.counter = 0

    def generate_id(self) -> int:
        with self.lock:
            self.counter += 1
            return int(time.time() * 1000) << 10 | self.counter
