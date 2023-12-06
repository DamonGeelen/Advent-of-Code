with open("input.txt", "r") as file:
    content = file.read()

lines = content.split("\n")

times = lines[0].split(":")[1].strip().split(" ")
times = [int(time) for time in times if time]

distances = lines[1].split(":")[1].strip().split(" ")
distances = [int(distance) for distance in distances if distance]

time_dist_dict = dict(zip(times, distances))

solution = 1
for time in time_dist_dict:
    count = 0
    for speed in range(time + 1):
        dist = speed * (time - speed)
        if dist > time_dist_dict[time]:
            count += 1
    solution *= count

print(f"If you mulitply these numbers together, you get {solution}.")