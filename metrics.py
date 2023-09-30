import os
import psutil
import time
import multiprocessing


def measure_memory_usage(process_id, interval):
    process = psutil.Process(process_id)
    while True:
        rss_memory = process.memory_info().rss / (1024 * 1024)
        cpu_percentage = process.cpu_percent(interval)
        with open('memory-usage.log', 'a') as memory:
            print(f"Memory usage: {rss_memory} MB", file=memory)
        with open('cpu-usage.log', 'a') as cpu:
            print(f"CPU usage: {cpu_percentage} %", file=cpu)
        time.sleep(interval)


def run_memory_metrics(interval):
    memory_process = multiprocessing.Process(
        target=measure_memory_usage,
        args=(os.getpid(), interval)
    )
    memory_process.start()
    return memory_process
