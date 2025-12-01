from typing import Callable
import time

import part_1 
import part_2_a
import part_2_b_brute_force


def time_my_task(task: Callable) -> None:

    print (f"Running: {task.__module__}")

    start = time.time()
    task("day-1\\input.txt")
    end = time.time()

    print(f"Time: {end - start:.4f} seconds\n")


if __name__ == "__main__":
    print()
    time_my_task(task=part_1.read_file_line_by_line)
    time_my_task(task=part_2_a.read_file_line_by_line)
    time_my_task(task=part_2_b_brute_force.read_file_line_by_line)