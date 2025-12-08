def resolve_line(line: str) -> int:
    line = line.strip()

    joltage_list = [0] * 12

    # scan once from left to right
    for i in range (len(line) - 11):

        swath = [int(char) for char in line[i:i+12]]   # [p, q, r, ...]

        for j in range(12):
            if swath[j] > joltage_list[j]:
                joltage_list[j] = swath[j]  # keep new biggest at each position
                joltage_list[j+1:] = [0] * (11 - j)  # reset all to the right

    joltage_string = ''.join(str(j) for j in joltage_list)  # pqr...
    return int(joltage_string)

def solve(filepath: str):
    total_joltage = 0
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            total_joltage += resolve_line(line)
    print(f"Answer: {total_joltage}")

if __name__ == "__main__":
    filename = ["examples",  # index 0
                "input"]     # index 1
    solve(f"2025\\day3\\{filename[1]}.txt")  # Change index to switch data set