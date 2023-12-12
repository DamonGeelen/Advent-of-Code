""" 
First, let's read the input into a string, and split it into a list of lines
with each element in the list representing a game. Note that we got rid of
the word "Game " at the beginning of each line, as it is unnneccesary for 
processing this data. 
"""
with open("input.txt", "r") as file:
    content = file.read()

content = content.replace("Game ", "")

games = content.split("\n")

"""
Next, let's create a dictionary that holds the data for each game. The value
of each game key will be a list of dictionaries which describe the outcome of
each round of each game.
"""
games_dict = {}

for game in games:

    game, rounds = game.split(":")
    rounds = rounds.split(";")

    round_list = []
    for round in rounds:

        round_split = round.split(",")
        round_strip = [round.strip() for round in round_split]

        round_dict = {
            "red" : 0,
            "green": 0,
            "blue": 0
            }
        for element in round_strip:
            value, key = element.split(" ")
            round_dict[key] = value
        
        round_list.append(round_dict)

    games_dict[game] = round_list

"""
Now we can iterate through the list to find the fewest possible cubes for each 
game, and find the sum of these powers.
"""
sum = 0

for game in games_dict:

    red = 0
    green = 0
    blue = 0

    for round in games_dict[game]:
        if int(round["red"]) > red:
            red = int(round["red"])
        
        if int(round["green"]) > green:
            green = int(round["green"])

        if int(round["blue"]) > blue:
            blue = int(round["blue"])
        
    power = red * green * blue
    sum += power

print(f"The sum of the power of these sets is {sum}.")

