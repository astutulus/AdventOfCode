import time
from typing import Callable

import day_2.part_1 as part_1
import day_2.part_2_brute_force as part_2

def run_all(timer: Callable):

    data_path="day_2\\input.txt"

    timer(task=part_1.solve, data_path=data_path)
    timer(task=part_2.solve, data_path=data_path)
