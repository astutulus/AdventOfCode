def solve(filepath: str) -> int:
    timelines = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:

            # First row
            if not timelines:  
                for char in line:
                    if char == ".":
                        timelines.append(0)
                    elif char == "S":
                        timelines.append(1)
                        
            # All subsequent rows
            else:  
                for i, char in enumerate(line):
                    if char == "^" and timelines[i] > 0:
                        timelines[i-1] += timelines[i]  # Merge with left
                        timelines[i+1] += timelines[i]  # Merge with right
                        timelines[i] = 0                # Paths were split

    return sum(timelines)

if __name__ == "__main__":
    filename = ["debug",    # index 0
                "example",  # index 1
                "input"]    # index 2
    print(f"Answer: {solve(f"day7\\{filename[2]}.txt")}")  # Set filename