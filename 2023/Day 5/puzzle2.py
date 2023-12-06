def map_to(input, map):
    output = -1
    for element in map:
        if input >= int(element[1]) and input < int(element[1]) + int(element[2]):
                output = int(element[0]) + input - int(element[1])
                break
    if output == -1:
        output = input

    return output

def seed_search(start, range, step):

    min_location = float('inf')
    min_seed = float('inf')

    seed = start
    stop = seed + range
    if not range:
        seed = start - 1000*step
        stop = seed + 2000*step

    while seed < stop:
        soil = map_to(seed, seed_to_soil)
        fertilizer = map_to(soil, soil_to_fertilizer)
        water = map_to(fertilizer, fertilizer_to_water)
        light = map_to(water, water_to_light)
        temperature = map_to(light, light_to_temperature)
        humidity = map_to(temperature, temperature_to_humidity)
        location = map_to(humidity, humidity_to_location)

        if location < min_location:
            min_location = location
            min_seed = seed

        seed += step

    return min_location, min_seed

with open("input.txt", "r") as file:
    content = file.read()

# Format each map into a list of lists
maps = content.split("\n\n")

seeds = maps[0].split(":")[1].strip().split(" ")
seeds = [int(seed) for seed in seeds]

seed_to_soil = maps[1].split(":")[1].strip().split("\n")
seed_to_soil = [element.split(" ") for element in seed_to_soil]

soil_to_fertilizer = maps[2].split(":")[1].strip().split("\n")
soil_to_fertilizer = [element.split(" ") for element in soil_to_fertilizer]

fertilizer_to_water = maps[3].split(":")[1].strip().split("\n")
fertilizer_to_water = [element.split(" ") for element in fertilizer_to_water]

water_to_light = maps[4].split(":")[1].strip().split("\n")
water_to_light = [element.split(" ") for element in water_to_light]

light_to_temperature = maps[5].split(":")[1].strip().split("\n")
light_to_temperature = [element.split(" ") for element in light_to_temperature]

temperature_to_humidity = maps[6].split(":")[1].strip().split("\n")
temperature_to_humidity = [element.split(" ") for element in temperature_to_humidity]

humidity_to_location = maps[7].split(":")[1].strip().split("\n")
humidity_to_location = [element.split(" ") for element in humidity_to_location]

min_location = float('inf')
i = 0
while i < len(seeds) - 2:
    if seed_search(seeds[i], seeds[i + 1], 10000)[0] < min_location:
        min_location, min_seed = seed_search(seeds[i], seeds[i + 1], 10000)
    i += 2

min_location, min_seed = seed_search(min_seed, 0, 1000)
min_location, min_seed = seed_search(min_seed, 0, 100)
min_location, min_seed = seed_search(min_seed, 0, 10)
min_location, min_seed = seed_search(min_seed, 0, 1)

print(f"The lowest location number that corresponds to any of the initial seed numbers is {min_location}.")