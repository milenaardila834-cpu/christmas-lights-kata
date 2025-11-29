grid_size = 1000

instructions = [
    "turn on 887,9 through 959,629",
    "turn on 454,398 through 844,448",
    "turn off 539,243 through 559,965",
    "turn off 370,819 through 676,868",
    "turn off 145,40 through 370,997",
    "turn off 301,3 through 808,453",
    "turn on 351,678 through 951,908",
    "toggle 720,196 through 897,994",
    "toggle 831,394 through 904,860"
]

def parse_instruction(line):
    parts = line.split()
    if parts[0] == 'toggle':
        op = 'toggle'
        a = parts[1]
        b = parts[3]
    else:
        op = 'on' if parts[1] == 'on' else 'off'
        a = parts[2]
        b = parts[4]
    x1, y1 = map(int, a.split(','))
    x2, y2 = map(int, b.split(','))
    return op, x1, y1, x2, y2

grid = [[False] * grid_size for _ in range(grid_size)]

for line in instructions:
    op, x1, y1, x2, y2 = parse_instruction(line)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if op == 'on':
                grid[x][y] = True
            elif op == 'off':
                grid[x][y] = False
            else:
                grid[x][y] = not grid[x][y]

lights_on = sum(1 for row in grid for v in row if v)
print("Partie 1 - Lumières allumées:", lights_on)

brightness = [[0] * grid_size for _ in range(grid_size)]

for line in instructions:
    op, x1, y1, x2, y2 = parse_instruction(line)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if op == 'on':
                brightness[x][y] += 1
            elif op == 'off':
                if brightness[x][y] > 0:
                    brightness[x][y] -= 1
            else:
                brightness[x][y] += 2

total_brightness = sum(v for row in brightness for v in row)
print("Partie 2 - luminosité totale:", total_brightness)
