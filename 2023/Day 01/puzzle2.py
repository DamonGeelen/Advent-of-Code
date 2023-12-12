with open("input.txt", "r") as file:
    content = file.read()

# Replace written numbers with the numerical character.
# Note that the first and last letter are left in the string
# to preserve any overlapping number names (eg. "oneight")

content = content.replace('zero', 'z0o')
content = content.replace('one', 'o1e')
content = content.replace('two', 't2o')
content = content.replace('three', 't3e')
content = content.replace('four', 'f4r')
content = content.replace('five', 'f5e')
content = content.replace('six', 's6x')
content = content.replace('seven', 's7n')
content = content.replace('eight', 'e8t')
content = content.replace('nine', 'n9e')

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