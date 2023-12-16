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

sum = 0
for step in init_sequence:
    sum += HASH(step)

print(f"The sum of the results is {sum}.")