with open("input.txt", "r") as file:
    content = file.read()

list = content.split("\n")

list = [item[9:] for item in list]

winning_numbers = []
card_numbers = []

for item in list:
    item = item.split("|")
    winning_numbers.append(item[0].replace("  ", " 0").strip().split(" "))
    card_numbers.append(item[1].replace("  ", " 0").strip().split(" "))

total_points = 0

for i in range(len(list)):

    match_count = 0

    for number in winning_numbers[i]:
        if number in card_numbers[i]:
            match_count += 1
    
    if match_count == 0:
        continue

    else:
        total_points += 2**(match_count - 1)

print(f"They are worth {total_points} in total.")