def shortest_distance(a, b, empty_rows, empty_columns):
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])

    for row in empty_rows:
        if row in list(range(min(a[0], b[0]), max(a[0], b[0]))):
            distance += 999999
    
    for column in empty_columns:
        if column in list(range(min(a[1], b[1]), max(a[1], b[1]))):
            distance += 999999

    return distance

with open("input.txt", "r") as file:
    content = file.read()

lines = content.split("\n")

blank_rows = []
for i in range(len(lines)):
    if not "#" in lines[i]:
        blank_rows.append(i)

blank_columns = []
j = 0
while j < len(lines[0]):
    i = 0
    empty = True
    while empty and i < len(lines):
        if lines[i][j] == "#":
            empty = False
        i += 1
    if empty:
        blank_columns.append(j)
    j += 1

hash_locations = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            hash_locations.append([i, j])

sum = 0
for i in range(len(hash_locations) - 1):
    for j in range(i + 1, len(hash_locations)):
        sum += shortest_distance(hash_locations[i], hash_locations[j], blank_rows, blank_columns)

print(f"The sum of these lengths is {sum}.")