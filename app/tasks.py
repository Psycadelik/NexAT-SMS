import redis
import time

from rq import Queue

r = redis.Redis()
q = Queue(connection=r)


def send_sms():

    delay = 2
    time.sleep(delay)

#    job = q.enqueue(sms)
