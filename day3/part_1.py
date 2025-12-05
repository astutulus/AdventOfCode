def resolve_line(line: str) -> int:
    line = line.strip()

    joltage_tens, joltage_units = 0, 0

    # scan once from left to right
    for i in range (len(line) - 1):

        p = int(line[i])
        q = int(line[i + 1])

        if p > joltage_tens:
            joltage_tens = p  # keep the biggest 'tens'
            joltage_units = 0  # reset any units as will need to come from rhs
        if q > joltage_units:
            joltage_units = q  # keep the biggest units SINCE the biggest tens

    return joltage_tens * 10 + joltage_units

def solve(filepath: str):
    total_joltage = 0
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            total_joltage += resolve_line(line)
    print(f"Answer: {total_joltage}")

if __name__ == "__main__":
    filename = ["examples",  # index 0
                "input"]     # index 1
    solve(f"day3\\{filename[1]}.txt")  # Change index to switch data set