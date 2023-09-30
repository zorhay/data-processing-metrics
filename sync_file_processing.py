import time
import requests

from metrics import run_memory_metrics
from utils import get_randomized_path


def download_pipe_write(url: str, path: str) -> None:
    chunk_size = 1024*100
    with requests.get(url, stream=True) as resp:
        with open(path, 'wb') as file:
            for chunk in resp.iter_content(chunk_size):
                file.write(chunk)


def download_then_write(url: str, path: str) -> None:
    binary_data = requests.get(url).content
    with open(path, 'wb') as file:
        file.write(binary_data)


if __name__ == "__main__":

    metrics_process = run_memory_metrics(1)

    url = 'http://ipv4.download.thinkbroadband.com/50MB.zip'
    local_url = 'http://192.168.10.43:80/1GB.bin'
    path = get_randomized_path('data', 'test.zip')

    start_time = time.time()
    download_then_write(local_url, path)
    # download_pipe_write(local_url, path)
    end = time.time() - start_time
    print(end)

    metrics_process.terminate()
    metrics_process.join()

