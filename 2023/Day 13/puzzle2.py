def line_of_reflection(array):

    for n in range(1, len(array)//2 + 1):
        
        a = array[:n]
        b = array[n:2*n][::-1]
        diff = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] != b[i][j]:
                    l_o_r = n
                    diff += 1
        
        if diff == 1:
            return l_o_r
        
        a = array[-n:]
        b = array[-2*n:-n][::-1]
        diff = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] != b[i][j]:
                    l_o_r = len(array) - n
                    diff += 1
        
        if diff == 1:
            return l_o_r

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