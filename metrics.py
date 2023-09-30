import os
import psutil
import time
import multiprocessing


def measure_memory_usage(process_id, interval):
    process = psutil.Process(process_id)
    while True:
        memory_info = process.memory_info()
        rss_memory = memory_info.rss / (1024 * 1024)
        with open('log.txt', 'a') as log:
            print(f"Memory usage: {rss_memory} MB", file=log)
        time.sleep(interval)


def run_memory_metrics(interval):
    memory_process = multiprocessing.Process(
        target=measure_memory_usage,
        args=(os.getpid(), interval)
    )
    memory_process.start()
    return memory_process
