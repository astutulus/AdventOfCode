def count_invalid_id(first: str, last: str) -> int:

    invalid_id_sum = 0

    first_id_len = len(first)
    last_id_len = len(last)

    min_num = int(first)
    max_num = int(last)

    # Trim odd  lengths e.g. 7-700 need consider only 10-99
    if first_id_len % 2:
        min_num = pow(10, first_id_len)  # So 7 become 10
    if last_id_len % 2:
        max_num = pow(10, last_id_len - 1) - 1  # So 700 becomes 99

    half_len_of_min = int(len(str(min_num)) / 2)
    half_len_of_max = int(len(str(max_num)) / 2)

    check_from_half = int(str(min_num)[:half_len_of_min])
    check_to_half = int(str(max_num)[:half_len_of_max])

    for half in range(check_from_half, check_to_half + 1):
        
        first_half = half * pow(10, len(str(half)))  # e.g. from 74 obtain 7400

        check_num = first_half + half  # e.g. 7474

        if  min_num <= check_num and check_num <= max_num:
            invalid_id_sum += check_num

    return invalid_id_sum


def solve(data_path: str):

    with open(data_path, "r", encoding="utf-8") as file:
        data = file.readline().strip()
        ranges = data.split(',')

        answer = 0

        for range in ranges:
            bounds = range.split('-')
            count = count_invalid_id(first=bounds[0], last=bounds[1])
            answer += count

        print(f"Sum of invlid IDs in the input data: {answer}")

if __name__ == "__main__":
    solve()