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
Now we can iterate through the list to find which games would have been 
possible, and add these game numbers to our sum to find our answer.
"""
sum = 0

for game in games_dict:

    possible = True

    for round in games_dict[game]:
        if int(round["red"]) > 12 or int(round["green"]) > 13 or int(round["blue"]) > 14:
            possible = False

    if possible:
        sum += int(game)

print(f"The sum of the IDs of those games is {sum}.")

