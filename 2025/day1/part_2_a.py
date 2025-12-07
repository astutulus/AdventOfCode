dial_position = 50
zero_counter = 0

def resolve_line(line):
    global dial_position, zero_counter

    direction = line[0]
    distance = int(line[1:])

    # Clockwise (simples)
    if direction == "R":
        dial_position += distance
        zero_counter += dial_position // 100  # Number of times passing zero
        dial_position %= 100  # Return dial to valid range

    # Anticlockwise (tricky)
    else:

        # Staying positive
        if distance < dial_position:
            dial_position -= distance

        # Borderline
        elif distance == dial_position:
            dial_position = 0
            zero_counter += 1

        # Going into the negative.
        else:

            # Pass zero at first?
            if dial_position > 0:
                zero_counter += 1  

            dial_position -= distance
            zero_counter += abs(dial_position) // 100  # Number of further times passing zero
            dial_position %= 100  # Return dial to valid range

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
    solve("day1\\input.txt")