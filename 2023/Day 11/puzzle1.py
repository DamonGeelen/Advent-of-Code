def shortest_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

with open("input.txt", "r") as file:
    content = file.read()

lines = content.split("\n")
i = 0
while i < len(lines):

    if not "#" in lines[i]:
        i += 1
        lines.insert(i, "." * len(lines[i]))

    i += 1

i = 0
j = 0
while j < len(lines[i]):

    empty = True
    for i in range(len(lines)):
        if lines[i][j] == "#":
            empty = False
            break
    
    if empty:
        j += 1
        for i in range(len(lines)):
            lines[i] = lines[i][:j] + "." + lines[i][j:]
    
    j += 1

hash_locations = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            hash_locations.append([i, j])

sum = 0
for i in range(len(hash_locations) - 1):
    for j in range(i + 1, len(hash_locations)):
        sum += shortest_distance(hash_locations[i], hash_locations[j])

print(f"The sum of these lengths is {sum}.")