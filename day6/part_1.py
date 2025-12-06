def solve(filepath: str):
    # Read file
    homework = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            # Trick for any number of spaces, split() with no args!
            homework.append(line.strip().split())

    # Last line contains the operators
    operators = homework.pop()

    # Add up the answer
    total = 0

    for i, operator in enumerate(operators):
        match operator:

            case '+':
                column_sum = 0
                for n in range(len(homework)):
                    column_sum += int(homework[n][i])
                total += column_sum

            case '*':
                column_product = 1
                for n in range(len(homework)):
                    column_product *= int(homework[n][i])
                total += column_product

            case _:
                print("Unknown operator: ", operator)

    print(f"Answer: {total}")

if __name__ == "__main__":
    filename = ["example", "input"]
    solve(f"day6\\{filename[1]}.txt")  # Change index to switch data set