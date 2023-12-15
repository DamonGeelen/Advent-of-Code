def north_tilt(lines):

    for i in range(1, len(lines)):

        for j in range(len(lines[i])):

            if lines[i][j] == "O":
                lines[i][j] = "."

                n = i - 1
                while n >= 0 and lines[n][j] == ".":
                    n -= 1

                lines[n + 1][j] = "O"
    
    return lines

def south_tilt(lines):

    for i in reversed(range(0, len(lines) - 1)):

        for j in range(len(lines[i])):

            if lines[i][j] == "O":
                lines[i][j] = "."

                n = i + 1
                while n < len(lines) and lines[n][j] == ".":
                    n += 1

                lines[n - 1][j] = "O"
    
    return lines

def west_tilt(lines):

    for i in range(len(lines)):

        for j in range(len(lines[i])):

            if lines[i][j] == "O":
                lines[i][j] = "."

                n = j - 1
                while n >= 0 and lines[i][n] == ".":
                    n -= 1

                lines[i][n + 1] = "O"
    
    return lines

def east_tilt(lines):

    for i in range(len(lines)):

        for j in reversed(range(0, len(lines[i]) - 1)):

            if lines[i][j] == "O":
                lines[i][j] = "."

                n = j + 1
                while n < len(lines[i]) and lines[i][n] == ".":
                    n += 1

                lines[i][n - 1] = "O"
    
    return lines

def spin_cycle(lines):

    lines = north_tilt(lines)

    lines = west_tilt(lines)

    lines = south_tilt(lines)

    lines = east_tilt(lines)

    return(lines)


def total_load(lines):

    total_load = 0
    for i in range(len(lines)):

        for j in range(len(lines)):

            if lines[i][j] == "O":
                total_load += len(lines) - i
    
    return total_load

with open("input.txt", "r") as file:
    content = file.read()

lines = content.split("\n")

for i in range(len(lines)):
    lines[i] = list(lines[i])


load_sequence = []
for i in range(0, 200):
    lines = spin_cycle(lines)
    load_sequence.append(total_load(lines))

i = 2
while i < len(load_sequence)/2:
    if load_sequence[-i:] == load_sequence[-i*2:-i]:
        pattern = load_sequence[-i:]
        pattern_length = i
        break
    i += 1

billionth_load = pattern[(1000000000 - 200) % len(pattern) - 1]

print(f"The total load on the north support beams after 1,000,000,000 cycles is {billionth_load}.")