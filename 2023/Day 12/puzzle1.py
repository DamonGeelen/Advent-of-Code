def arrangement_check(row, actual_key):

    this_key = []
    count = 0
    for i in range(len(row)):
        if row[i] == "#":
            count += 1
            if i == len(row) - 1:
                this_key.append(count)

        else:
            if count:
                this_key.append(count)
                count = 0

    return this_key == actual_key

def possible_rows(row, key, damaged_missing):
    
    count = 0
    row = list(row)
    new_damaged_missing = damaged_missing
    for char in row:
        if char == "#":
            new_damaged_missing -= 1
    
    if new_damaged_missing <= 0:
        if arrangement_check("".join(row), key):
            count += 1
        return count

    for i in range(len(row)):
        if row[i] == "?":
            row[i] = "#"
            count += possible_rows("".join(row), key, damaged_missing)
            row[i] = "."
        if i == len(row) - 1:
            return count

with open("input.txt", "r") as file:
    content = file.read()

lines = content.split("\n")

rows = [line.split(" ")[0] for line in lines]
keys = []
for line in lines:
    key = []
    for char in line.split(" ")[1].split(","):
        key.append(int(char))
    keys.append(key)

total_count = 0
for i in range(len(rows)):
    total_count += possible_rows(rows[i], keys[i], sum(keys[i]))
print(total_count)