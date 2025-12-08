def solve(filepath: str) -> int:
    # Count tachylon splits
    splits = 0
    with open(filepath, "r", encoding="utf-8") as file:
        beams = []
        for line in file:
            # First row
            if not beams:  
                for char in line:
                    if char == ".":
                        beams.append(False)
                    elif char == "S":
                        beams.append(True)
            # All subsequent rows
            else:  
                for i, char in enumerate(line):
                    if char == "^" and beams [i]:
                        beams[i-1] |= True  # OR left beam
                        beams[i] = False  # Block incoming beam
                        beams[i+1] |= True  # OR right beam
                        splits += 1
    return splits

if __name__ == "__main__":
    filename = ["debug",    # index 0
                "example",  # index 1
                "input"]    # index 2
    print(f"Answer: {solve(f"2025\\day7\\{filename[2]}.txt")}")  # Set filename