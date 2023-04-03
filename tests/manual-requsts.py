from threading import Thread
from multiprocessing import Process
import threading
import multiprocessing

import requests
import json

from time import sleep
from random import randint

def process_func():
    threads = []
    for i in range(1, 200000):
        print(f'From {multiprocessing.current_process()} - {i}')
        threads.append(Thread(target=thread_func))
        
    for t in threads:
        t.start()
        sleep(randint(1, 5))
    for t in threads:
        t.join()
        
def thread_func():
    while True:
        p = {
            "title": "string",
            "content": "string",
            "is_published": True
        }
        
        status = requests.post(url='http://0.0.0.0:8000/posts/create', json=p)
        
        print(status)
        
        # status = requests.get(url='http://0.0.0.0:8000/posts/')
        # print(status)
        
        
        

if __name__ == '__main__':
    processes = []
    for i in range(1, 17):
        processes.append(Process(target=process_func))
        
    for p in processes:
        p.start()
        
    for p in processes:
        p.join()