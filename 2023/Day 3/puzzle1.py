def is_symbol(char):

    if not char.isnumeric() and not char == ".":
        return True
    
    else:
        return False


with open("input.txt", "r") as file:
    content = file.read()

lines = content.split("\n")

sum = 0

for i in range(len(lines)):

    adj_to_symbol = False
    current_num = ""

    for j in range(len(lines[i])):

        if lines[i][j].isnumeric():

            current_num += lines[i][j]

            if not adj_to_symbol:

                if i > 0:
                    if j > 0 and is_symbol(lines[i - 1][j - 1]):
                        adj_to_symbol = True

                    elif is_symbol(lines[i - 1][j]):
                        adj_to_symbol = True

                    elif j < len(lines[i]) - 1 and is_symbol(lines[i - 1][j + 1]):
                        adj_to_symbol = True
                
                if j > 0 and is_symbol(lines[i][j - 1]):
                    adj_to_symbol = True
                
                if j < len(lines[i]) - 1 and is_symbol(lines[i][j + 1]):
                    adj_to_symbol = True
                
                if i < len(lines) - 1:
                    if j > 0 and is_symbol(lines[i + 1][j - 1]):
                        adj_to_symbol = True

                    elif is_symbol(lines[i + 1][j]):
                        adj_to_symbol = True

                    elif j < len(lines[i]) - 1 and is_symbol(lines[i + 1][j + 1]):
                        adj_to_symbol = True

        else:

            if adj_to_symbol and current_num:
                sum += int(current_num)
            
            adj_to_symbol = False
            current_num = ""

        if j == len(lines[i]) - 1:

            if adj_to_symbol and current_num:
                sum += int(current_num)
        
print(f"The sum of all of the part numbers in the engine schematic is {sum}.")