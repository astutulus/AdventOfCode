import time
from typing import Callable


def elf_timer(task: Callable, data_path: str) -> None:

    print (f"Running: {task.__module__}")

    start = time.time()
    task(data_path)  # Execute task
    end = time.time()

    print(f"Time: {end - start:.4f} seconds\n")