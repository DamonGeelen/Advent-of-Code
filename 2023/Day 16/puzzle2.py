def move(i, j , direction, map):

    match direction:
        case 'R':
            j += 1
        
        case 'L':
            j -= 1
        
        case 'U':
            i -= 1

        case 'D':
            i += 1

    if i < 0 or i >= len(map):
        return None

    if j < 0 or j >= len(map[i]):
        return None

    return [i, j, direction] 
        
def energized_tiles(starting_beam, map):
    map_trace = [[]]
    for i in range(len(map[0])):
        map_trace[0].append(0)

    for i in range(len(map) - 1):
        map_trace.append(map_trace[0].copy())

    beams = [starting_beam]
    beam_history = [None]

    while len(beams):

        curr_beam = beams[0]
        beam_history.append(curr_beam)
        [i, j , direction] = curr_beam
        map_trace[i][j] = 1

        if map[i][j] != '.':
            match map[i][j]:
                case '/':
                    match direction:
                        case 'R':
                            direction = 'U'

                        case 'L':
                            direction = 'D'

                        case 'U':
                            direction = 'R'

                        case 'D':
                            direction = 'L'
                
                case '\\':
                    match direction:
                        case 'R':
                            direction = 'D'

                        case 'L':
                            direction = 'U'

                        case 'U':
                            direction = 'L'

                        case 'D':
                            direction = 'R'
                
                case '|':
                    if direction == 'R' or direction == 'L':
                        direction = 'U'
                        beams.append([i, j, 'D'])
                
                case '-':
                    if direction == 'U' or direction == 'D':
                        direction = 'R'
                        beams.append([i, j, 'L'])

        beams[0] = move(i, j, direction, map)

        if beams[0] in beam_history:
            beams = beams[1:]
            

    count = 0
    for line in map_trace:
        for tile in line:
            if tile:
                count += 1

    return count

with open('input.txt', 'r') as file:
    content = file.read()

map = content.split("\n")

for line in map:
    line = list(line)

max_count = 0

starting_beams = []
for i in range(len(map)):
    starting_beams.append([i, 0, 'R'])
    starting_beams.append([i, len(map[i]) - 1, 'L'])

for j in range(len(map[0])):
    starting_beams.append([len(map) - 1, j, 'U'])
    starting_beams.append([0, j, 'D'])

max_count = 0
i = 0
for beam in starting_beams:
    # Progress tracker
    print(f"{i}/{len(starting_beams)}")
    
    max_count = max([max_count, energized_tiles(beam, map)])
    i += 1

print(f"{max_count} tiles end up being energized.")