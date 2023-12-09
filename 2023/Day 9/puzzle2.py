def extrapolate(sequence):
    
    next_sequence = []
    for i in range(len(sequence) - 1):
        next_sequence.append(sequence[i + 1] - sequence[i])
    
    end_of_recursion = True
    for value in sequence:
        if value:
            end_of_recursion = False
            break
    
    if end_of_recursion:
        return(0)

    sequence.insert(0, sequence[0] - extrapolate(next_sequence))
    
    return sequence[0]
    


with open("input.txt", "r") as file:
    content = file.read()

lines = content.split("\n")

histories = [line.split(" ") for line in lines]
sum = 0
for sequence in histories:
    sequence = [int(value) for value in sequence]
    sum += extrapolate(sequence)

print(f"The sum of these extrapolated values is {sum}.")