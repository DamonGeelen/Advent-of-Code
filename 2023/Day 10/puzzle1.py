def find_start(map):

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                return i, j
    
    return None


with open("input.txt", "r") as file:
    content = file.read()

map = content.split("\n")

i, j = find_start(map)

prev_i = i
prev_j = j

count = 0

if map[i - 1][j] == "|" or map[i - 1][j] == "F" or map[i - 1][j] == "7":
    i -= 1
    count += 1

elif map[i][j + 1] == "-" or map[i][j + 1] == "J" or map[i][j + 1] == "7":
    j += 1
    count += 1

elif map[i + 1][j] == "|" or map[i + 1][j] == "J" or map[i + 1][j] == "L":
    i += 1
    count += 1

elif map[i][j - 1] == "-" or map[i + 1][j] == "F" or map[i + 1][j] == "L":
    j -= 1
    count += 1

char = map[i][j]
while char != "S":

    match char:

        case "|":
            if prev_i < i:
                prev_i = i
                i += 1
            else:
                prev_i = i
                i -= 1

        case "-":
            if prev_j < j:
                prev_j = j
                j += 1
            else:
                prev_j = j
                j -= 1
            
        case "L":
            if prev_i == i:
                prev_j = j
                i -= 1
            else:
                prev_i = i
                j += 1
        
        case "J":
            if prev_i == i:
                prev_j = j
                i -= 1
            else:
                prev_i = i
                j -= 1
        
        case "7":
            if prev_i == i:
                prev_j = j
                i += 1
            else:
                prev_i = i
                j -= 1

        case "F":
            if prev_i == i:
                prev_j = j
                i += 1
            else:
                prev_i = i
                j += 1

    char = map[i][j]
    count += 1

print(f"It takes {int(count/2)} steps along the loop to get from the starting position to the point farthest from the starting position.")