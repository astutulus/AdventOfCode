def solve(data_path: str):

    # Info to be read from file
    fresh_ingredient_ranges = []
    available_ingredients = []

    # Flag which info is being read
    reading_fresh_ingredients = True  

    # Read file
    with open(data_path, "r", encoding="utf-8") as file:
        for line in file:
            if reading_fresh_ingredients:
                if line.strip() == "":
                    # Flip flag on blank line
                    reading_fresh_ingredients = False
                else:
                    # Parse range as integer tuple
                    range_limits = line.strip().split("-")
                    fresh_from, fresh_to = map(int, range_limits)
                    fresh_ingredient_ranges.append((fresh_from, fresh_to))
            else:
                # Parse available ingredient as integer
                available_ingredients.append(int(line.strip()))

    count_available_ingredients_that_are_fresh = 0

    # Check each available ingredient against fresh ingredient ranges
    for i in available_ingredients:
        for fresh_range in fresh_ingredient_ranges:
            fresh_from, fresh_to = fresh_range
            if fresh_from <= i <= fresh_to:
                count_available_ingredients_that_are_fresh += 1
                break  # No need to check other ranges for this ingredient

    print(f"Answer: {count_available_ingredients_that_are_fresh}")

#solve("day5\\example.txt")
solve("day5\\input.txt")