def merge_overlapping_tuples(t1, t2):
    # Merge overlapping tuples, including if they butt up (albeit that
    # case could equally be left separate for purpose of this problem)
    # 
    # For simplicity assume "sorted" i.e. t1[0] <= t2[0]
    #
    #  t1[0]---------------t1[1]
    #           t2[0]---------------t2[1]
    #
    #
    if t1[1] < (t2[0] - 1):
        return None  # No overlap and don't butt up
    else:
        return (min(t1[0], t2[0]), max(t1[1], t2[1]))

def solve(filepath: str):
    
    fresh_ranges = []

    # Read ranges from file
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() == "":
                # Data after blank line is redundant for part 2
                break  
            else:
                # Parse range as integer tuple
                range_limits = line.strip().split("-")
                fresh_from, fresh_to = map(int, range_limits)
                fresh_ranges.append((fresh_from, fresh_to))

    fresh_ranges.sort()

    # Merge overlaps starting with first element
    merged_ranges = [fresh_ranges[0]]

    # Continue from second element
    for i, range in enumerate(fresh_ranges):
        if i > 0:
            merged = merge_overlapping_tuples(merged_ranges[-1], range)
            if merged:
                # Replace last element with merged range
                merged_ranges[-1] = merged
            else:
                merged_ranges.append(range)

    # Sum all ranges
    count_fresh_ids = 0
    for i in merged_ranges:
        count_fresh_ids += i[1] - i[0] + 1  # Inclusive range
    print(f"Answer: {count_fresh_ids}")

if __name__ == "__main__":
    filename = ["example",  # index 0
                "input"]    # index 1
    solve(f"day5\\{filename[1]}.txt")  # Change index to switch data set