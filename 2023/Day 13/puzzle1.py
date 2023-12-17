def line_of_reflection(array):

    for i in range(1, len(array)//2 + 1):
        
        a = array[:i]
        b = array[i:2*i]
        if a == b[::-1]:
            return i
        
        a = array[-i:]
        b = array[-2*i:-i]
        if a == b[::-1]:
            return len(array) - i

    return 0

with open('input.txt', 'r') as file:
    content = file.read()

arrays = content.split('\n\n')

for i in range(len(arrays)):
    arrays[i] = arrays[i].split('\n')
    for j in range(len(arrays[i])):
        arrays[i][j] = list(arrays[i][j])


summary = 0
for array in arrays:
    summary += 100 * line_of_reflection(array) + line_of_reflection(list(zip(*array)))

print(f'The final number after summarizing all notes is {summary}.')