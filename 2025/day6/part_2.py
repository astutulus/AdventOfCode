def solve(filepath: str):
    # Read file
    homework = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            homework.append(line)

    # Consider row lengths
    longest_row_length = 0
    for row in homework:
        len_row = len(row)
        print(f"Row length: {len_row}")
        if len_row > longest_row_length:
            longest_row_length = len_row

    # Last line contains the operators
    operators = homework.pop()

    # Add up the answer
    total = 0

    # Scan all homework by column index from left to right
    i = 0

    there_is_data = True
    while there_is_data:

        reading_problem = True
        problem_operator = ''
        problem_operands = []

        while reading_problem:
            # Read operator
            try:
                op = operators[i]
            except IndexError:
                print("End of data for operators")

            if op == '+' or op == '*':
                if problem_operator:
                    print("Already got an operator")
                else:
                    problem_operator = op

            # Read operands
            found_digits = False
            operand_string = ""
            for row in homework:

                try:
                    char = row[i]
                except IndexError:
                    print(f"End of data for operatorand row {row}")

                if char not in [' ', '\n']:
                    found_digits = True
                    operand_string += char

            if found_digits: 
                problem_operands.append(int(operand_string))
            else:
                # Must have been a column of spaces or newlines
                reading_problem = False

            # In either case, march onwards
            i += 1

        # Finished reading problem; now to solve it.
        match problem_operator:

            case '+':
                column_sum = 0
                for n in problem_operands:
                    column_sum += n
                total += column_sum
                # 
                # print(f"Added {problem_operands} = {column_sum}")
                # 
            case '*':
                column_product = 1
                for n in problem_operands:
                    column_product *= n
                total += column_product
                # 
                # print(f"Multiplied {problem_operands} = {column_product}")
                # 
            case _:
                print("Unknown operator: ", problem_operator)
                
        if i >= longest_row_length:
            there_is_data = False

    print(f"Answer: {total}")

if __name__ == "__main__":
    filename = ["example",  # index 0
                "input"]    # index 1
    solve(f"day6\\{filename[1]}.txt")  # Change index to switch data set