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

    qty_cells = len(elves_diagram)

    count = [0] * qty_cells

    # NW  N  NE
    #  W  @  E
    # SW  S  SE    
    west_neighbours = [-(width + 1), -1, width - 1]
    vert_neighbours = [-width, width]
    east_neighbours = [-(width - 1), 1, width + 1]

    # For each roll of paper, increment count of all neighbouring cells
    def count_neighbours_for_whole_diagram():
        for cell in range(qty_cells):
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
                    if 0 <= neighbour < qty_cells:
                        count[neighbour] += 1

    # Remove accessible rolls of paper
    # Return how many were removed
    def remove_accessible_rolls() -> int:
        removed = 0
        for cell in range(qty_cells):
            if elves_diagram[cell] == "@" and count[cell] < 4:
                elves_diagram[cell] = "."
                removed += 1
        return removed

    forklifts_working = True
    total_rolls_removed = 0

    while forklifts_working:
        # Reset counts
        count = [0] * qty_cells  
        count_neighbours_for_whole_diagram()

        rolls_removed = remove_accessible_rolls()
        if rolls_removed:
            total_rolls_removed += rolls_removed
        else:
            forklifts_working = False

    print(f"Total rolls of paper removed: {total_rolls_removed}")

if __name__ == "__main__":
    filename = ["debug",     # index 0
                "example",   # index 1
                "input"]     # index 2
    solve(f"2025\\day4\\{filename[2]}.txt")  # Change index to switch data set