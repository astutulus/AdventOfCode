import sys

def solve_reccursively(lights: int, 
                    wiring: list[int],
                    used: list[int],
                    best_found: int) -> int:

    for i in range(len(wiring)):
        wires = wiring[i]
        
        new_used = used.copy()
        new_used.append(wires)

        # Try as base case
        result = lights ^ wires
        if not result:
            # print (f"Solved with: {new_used}")
            best_found = min(best_found, len(new_used))
        
        # Reccurse
        else:
            # Create a new list without the i-th element
            remainder = wiring[:i] + wiring[i+1:]
            best_found = solve_reccursively(lights=result, 
                                wiring=remainder,
                                used=new_used,
                                best_found=best_found)
            
    return best_found

# Try all permutations of the binary representations 
def solve_machine(lights: int, 
                  wiring: list[int], 
                  joltage: list[int]) -> int:

    # print (f"Lights:  {lights}")
    # print (f"Wiring:  {wiring}")
    # print (f"Joltage: {joltage}\n")

    return solve_reccursively(lights=lights, 
                            wiring=wiring,
                            used=[],
                            best_found=sys.maxsize)


# Parse each line of instruction manual to a binary form
def solve(filepath: str):
    answer = 0
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            manual = line.strip().split(' ')
            lights: int = 0
            light_bits = 0
            wiring: list[int] = []
            joltage: list[int] = []
            for data in manual:
                match data[0]:
                    case '[':
                        light_diagram = data[1:-1]  # Remove brackets
                        light_bits = len(light_diagram)
                        light_diagram = light_diagram.replace('.', '0')
                        light_diagram = light_diagram.replace('#', '1')
                        lights = int(light_diagram, 2)  # Convert binary string to base 10
                    case '(':
                        button_mask = 0
                        for button in data[1:-1].split(','):
                            binary_string = '1' + '0' * (light_bits - int(button) - 1)
                            button_mask += int(binary_string, 2)

                        wiring.append(button_mask)
                    case '{':
                        joltage = [int(button) for button in data[1:-1].split(',')]
            best = solve_machine(lights=lights, wiring=wiring, joltage=joltage)
            print(best)
            answer += best

    return answer
            
if __name__ == "__main__":
    filename = ["debug",    # index 0
                "example",  # index 1
                "input"]    # index 2
    print(f"Answer: {solve(f"2025\\day10\\{filename[2]}.txt")}")  # Set filename 