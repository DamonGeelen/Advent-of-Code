with open("input.txt", "r") as file:
    content = file.read()

lines = content.split("\n")

for i in range(len(lines)):
    lines[i] = list(lines[i])

for i in range(1, len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "O":
            lines[i][j] = "."
            n = i - 1
            while n >= 0 and lines[n][j] == ".":
                n -= 1
            lines[n + 1][j] = "O"

total_load = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if lines[i][j] == "O":
            total_load += len(lines) - i

print(f"The total load on the north support beams is {total_load}.")