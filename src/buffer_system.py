import threading
from queue import Queue

buffer = Queue(maxsize=10)

empty = threading.Semaphore(10)
full = threading.Semaphore(0)
mutex = threading.Lock()

