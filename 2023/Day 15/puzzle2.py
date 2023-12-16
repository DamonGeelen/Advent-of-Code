def HASH(str):
    current_value = 0
    for char in str:
        if char == "\n":
            continue
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

with open("input.txt", "r") as file:
    content = file.read()

init_sequence = content.split(",")

boxes = []
for i in range(256):
    boxes.append([])

for step in init_sequence:
    label = ""
    for char in step:
        if char.isalpha():
            label += char
        elif char == "-":
            if not boxes[HASH(label)]:
                continue
            if not boxes[HASH(label)][0]:
                continue
            else:
                for lens in boxes[HASH(label)]:
                    if lens[0] == label:
                        boxes[HASH(label)].remove(lens)

        elif char == "=":
            label_is_in_box = False
            for lens in boxes[HASH(label)]:
                if lens[0] == label:
                        lens[1] = int(step[-1])
                        label_is_in_box = True
            if not label_is_in_box:
                boxes[HASH(label)].append([label, int(step[-1])])


focusing_power = 0
for i in range(len(boxes)):
    if boxes[i]:
        for j in range(len(boxes[i])):
            focusing_power += (i + 1) * (j + 1) * boxes[i][j][1]

print(f"The focusing power of the resulting lens configuration is {focusing_power}.")