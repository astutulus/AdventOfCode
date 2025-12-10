def solve(filepath: str):
    points = []
    answer = 0
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:

            # Read new point as list of int
            new = [int(n) for n in line.strip().split(',')]

            # Compare with each existing point
            for p in points:
                area = (abs(new[0] - p[0]) + 1) * (abs(new[1] - p[1]) + 1)
                if area > answer:
                    answer = area

            # Add new to existing
            points.append(new)

    return answer
            
if __name__ == "__main__":
    filename = ["example",  # index 0
                "input"]    # index 1
    print(f"Answer: {solve(f"2025\\day9\\{filename[1]}.txt")}")  # Set filename 