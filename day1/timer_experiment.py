import time
from typing import Callable

import part_1
import part_2_a
import part_2_b_brute_force

# Time a given function (that takes a given filepath as its sole argument).
def elf_timer(task: Callable, filepath: str) -> float:
    print (f"Running module: {task.__module__}")
    start = time.time()
    task(filepath)  # Call task
    end = time.time()
    return end - start

if __name__ == "__main__":
    tasks = [part_1.solve,
            part_2_a.solve,
            part_2_b_brute_force.solve]
    
    for task in tasks:
        execution_time = elf_timer(task=task, filepath="day1\\input.txt")
        print(f"Time: {execution_time:.4f} seconds\n")