from src.producer_logic import producer
from src.consumer_logic import consumer
import threading

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()

p.join()
c.join()

