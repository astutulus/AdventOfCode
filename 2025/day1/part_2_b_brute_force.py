dial_position = 50
zero_counter = 0

def resolve_line(line):
    global dial_position, zero_counter

    direction = line[0]
    distance = int(line[1:])

    # Clockwise
    if direction == "R":
        for _ in range (distance):
            dial_position += 1
            if dial_position == 100:
                dial_position = 0
                zero_counter += 1

    # Anticlockwise
    else:
        for _ in range (distance):
            dial_position -= 1
            if dial_position == 0:
                zero_counter += 1
            if dial_position == -1:
                dial_position = 99

def solve(filepath):
    # Read file line by line
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                resolve_line(line)
    except FileNotFoundError:
        print(f"Input file '{filepath}' not found")

    print (f"Answer: {zero_counter}")

if __name__ == "__main__":
    solve("2025\\day1\\input.txt")