def solve(filepath: str):
    elves_diagram = []

    # Not elegant, but doesn't cost as only called once
    with open(filepath, "r", encoding="utf-8") as file:
        width = len(file.readline().strip())

    # Read the entire diagram into a single list
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            for char in line.strip():
                elves_diagram.append(char)

    count = [0] * len(elves_diagram)

    # NW  N  NE
    #  W  @  E
    # SW  S  SE    
    west_neighbours = [-(width + 1), -1, width - 1]
    vert_neighbours = [-width, width]
    east_neighbours = [-(width - 1), 1, width + 1]

    # For each roll of paper, increment count of all neighbouring cells
    for cell in range(len(elves_diagram)):
        if elves_diagram[cell] == "@":

            # If cell is at edge then don't include neighbours that would wrap around
            if cell % width == 0:  # west edge
                neighbours = vert_neighbours + east_neighbours
            elif cell % width == width - 1:  # east edge
                neighbours = west_neighbours + vert_neighbours
            else:
                neighbours = west_neighbours + vert_neighbours + east_neighbours

            for n in neighbours:
                neighbour = cell + n
                # Confirm still within diagram (when handling top and bottom rows)
                if 0 <= neighbour < len(elves_diagram):
                    count[neighbour] += 1

    # Output the answer
    qty_rolls_accessible = 0
    for cell in range(len(elves_diagram)):
        if elves_diagram[cell] == "@" and count[cell] < 4:
            qty_rolls_accessible += 1
    print(f"Quantity of rolls accessible: {qty_rolls_accessible}")

if __name__ == "__main__":
    filename = ["debug",     # index 0
                "example",   # index 1
                "input"]     # index 2
    solve(f"2025\\day4\\{filename[2]}.txt")  # Change index to switch data set