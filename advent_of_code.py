from elf_timer import elf_timer

import day_1.main
import day_2.main

if __name__ == "__main__":

    day_num = input("Enter day number to run solutions with timer: ")
    print()
    match int(day_num):
        case 1:
            day_1.main.run_all(timer=elf_timer)
        case 2:
            day_2.main.run_all(timer=elf_timer)