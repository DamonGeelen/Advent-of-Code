with open("input.txt", "r") as file:
    content = file.read()

lines = content.split("\n")

time = int(lines[0].split(":")[1].replace(" ", ""))
record = int(lines[1].split(":")[1].replace(" ", ""))

count = 0
for speed in range(time + 1):
    dist = speed * (time - speed)
    if dist > record:
        count += 1


print(f"There are {count} ways to beat the record in this one much longer race.")