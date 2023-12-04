with open("input.txt", "r") as file:
    content = file.read()

sum = 0
first_number = last_number = -1

for char in content:

    if char.isnumeric():

        if first_number == -1:
            first_number = last_number = char

        else:
            last_number = char
        
    if char == "\n":

        if first_number == -1 or last_number == -1:
            print("Error in detecting first or last number in line.")

        sum += int(first_number + last_number)
        first_number = last_number = -1

print(f"The sum of all of the calibration values is {sum}.")