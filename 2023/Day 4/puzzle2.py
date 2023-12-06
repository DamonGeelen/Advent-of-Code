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

card_ids = [id for id in range(1, len(list) + 1)]

card_instances = [1] * len(card_ids)

card_dict = dict(zip(card_ids, card_instances))

total_cards = 0
for id in card_ids:

    total_cards += card_dict[id]
    match_count = 0

    for number in winning_numbers[id - 1]:
        if number in card_numbers[id - 1]:
            match_count += 1
    
    if match_count > 0:
        for i in range(1, match_count + 1):
            card_dict[id + i] += card_dict[id]

    i += 1

print(f"You would end up with {total_cards} total scratchcards.")