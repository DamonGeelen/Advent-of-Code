# Function to determine the type of hand
def hand_type(hand):

    hand = list(hand)
    matches = {}

    for i in range(len(hand) - 1):

        for j in range(i + 1, len(hand)):

            if hand[i] != "J" and hand[i] == hand[j]:

                if hand[i] not in matches:
                    matches[hand[i]] = 2
                    hand[j] = " "

                else:
                    matches[hand[i]] += 1
                    hand[j] = " "
    
    if " " in  matches:
        del matches[" "]

    if not matches:
        if "J" in hand:
            matches = {"J": hand.count("J") + 1}
    
    else:
        matches[list(matches.keys())[0]] += hand.count("J")

    if len(matches) == 1:
        for card in matches:
            if matches[card] == 2:
                return "One Pair"
            elif matches[card] == 3:
                return "Three Of A Kind"
            elif matches[card] == 4:
                return "Four Of A Kind"
            else: 
                return "Five Of A Kind"
            
    elif len(matches) == 2:
        for card in matches:
            if matches[card] == 3:
                return "Full House"
        
        return "Two Pair"
    
    return "High Card"

# Function to use as a key for the sorted() function
def sorting_key(hand):
    cards = []
    for card in hand:
        if card.isnumeric():
            cards.append(int(card))
        
        else:
            match card:
                case "T":
                    cards.append(10)
                
                case "J":
                    cards.append(1)
                
                case "Q":
                    cards.append(12)
                 
                case "K":
                    cards.append(13)

                case "A":
                    cards.append(14)
    
    return tuple(cards)
    

# Read input and process it into a dictionary
# of hands and bids
with open("input.txt", "r") as file:
    content = file.read()

lines = content.split("\n")
hand = []
bid = []
for line in lines:
    line = line.split(" ")
    hand.append(line[0])
    bid.append(line[1])
hands_dict = dict(zip(hand, bid))

# Create a dictionary for each type of hand and 
# fill it with the hands from the input
high_card = []
one_pair = []
two_pair = []
three_of_a_kind = []
full_house = []
four_of_a_kind = []
five_of_a_kind = []

for hand in hands_dict:

    match hand_type(hand):

        case "High Card":
            high_card.append(hand)

        case "One Pair":
            one_pair.append(hand)

        case "Two Pair":
            two_pair.append(hand)

        case "Three Of A Kind":
            three_of_a_kind.append(hand)

        case "Full House":
            full_house.append(hand)

        case "Four Of A Kind":
            four_of_a_kind.append(hand)
        
        case "Five Of A Kind":
            five_of_a_kind.append(hand)

sorted_hands_list = sorted(high_card, key = sorting_key) + \
                    sorted(one_pair, key = sorting_key) + \
                    sorted(two_pair, key = sorting_key) + \
                    sorted(three_of_a_kind, key = sorting_key) + \
                    sorted(full_house, key = sorting_key) + \
                    sorted(four_of_a_kind, key = sorting_key) + \
                    sorted(five_of_a_kind, key = sorting_key)

print("High Card:", high_card, "\n")
print("One Pair:", one_pair, "\n")
print("Two Pair:", two_pair, "\n")
print("Three Of A Kind:", three_of_a_kind, "\n")
print("Full House:", full_house, "\n")
print("Four Of A Kind:", four_of_a_kind, "\n")
print("Five Of A Kind:", five_of_a_kind, "\n")

winnings = 0
for i in range(len(sorted_hands_list)):
    winnings += (i + 1) * int(hands_dict[sorted_hands_list[i]])

print(f"The new total winnings are {winnings}.")