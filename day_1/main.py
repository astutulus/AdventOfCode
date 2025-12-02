from typing import Callable

import day_1.part_1 as pt_1
import day_1.part_2_a as pt_2a
import day_1.part_2_b_brute_force as pt_2b

def run_all(timer: Callable):

    data_path="day_1\\input.txt"

    timer(task=pt_1.read_file_line_by_line, data_path=data_path)
    timer(task=pt_2a.read_file_line_by_line, data_path=data_path)
    timer(task=pt_2b.read_file_line_by_line, data_path=data_path)
