def count_invalid_id(first: str, last: str) -> int:

    invalid_id_sum = 0

    min_num = int(first)
    max_num = int(last)

    for num in range(min_num, max_num + 1):
        str_num = str(num)
        length = len(str_num)


        for chunk_len in range(1, int(length / 2) + 1):

            if length % chunk_len != 0:
                continue

            chunks = [str_num[i:i + chunk_len] for i in range(0, length, chunk_len)]

            first_chunk = chunks[0]
            other_chunks = chunks[1:]

            all_same = True

            for chunk in other_chunks:
                if chunk != first_chunk:
                    all_same = False
                    break

            if all_same:
                invalid_id_sum += num
                break
    
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