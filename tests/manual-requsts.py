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
        sleep(1)
    for t in threads:
        t.join()
        
def thread_func():
    while True:
        p = {
            "email": "user@example.com",
            "password": "string"
        }
        
        requests.post(url='http://0.0.0.0:8000/login', json=p)
        
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
    
    # thread_func()