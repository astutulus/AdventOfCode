dial_position = 50
zero_counter = 0

def resolve_line(line):
    global dial_position, zero_counter

    direction = line[0]
    distance = int(line[1:]) % 100  # Multiple of 100 clicks can be ignored

    if direction == "R": 
        dial_position += distance
    elif direction == "L": 
        dial_position -= distance
        dial_position += 100
    else:
        print(f"Unrecognised prefix '{direction}'.")

    dial_position %= 100

    if dial_position == 0:
        zero_counter += 1

def read_file_line_by_line(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                resolve_line(line)
    except FileNotFoundError:
        print(f"Input file '{filepath}' not found")

    print (f"Answer: {zero_counter}")

if __name__ == "__main__":
    read_file_line_by_line("day-1\\input.txt")