# Initial values

land = [
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
    [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ]
]

m = len(land)
n = len(land[0])

bestPath = []
bestPathLen = 100000
path = []

def shortest_path():    #The main loop
    for i in range(m):
        if is_safe(i, 0):
            path.append((i, 0))
            find(i, 0) #It will fill the path array

def clear_the_map():
    for i in range(m):
        for j in range(n):
             if land[i][j] == 0:
                clear_sides(i, j) #Set the 4 sides of the cell to -1

def clear_sides(i, j):
    if i != 0:
        if land[i - 1][j] != 0: land[i - 1][j] = -1
    if i != m - 1:
        if land[i + 1][j] != 0: land[i + 1][j] = -1
    if j != n - 1:
        if land[i][j + 1] != 0: land[i][j + 1] = -1
    if j != 0:
        if land[i][j - 1] != 0: land[i][j - 1] = -1

def find(row, col):
    global bestPathLen
    if path[-1][1] == n - 1:
        if len(path) < bestPathLen:
            global bestPath
            bestPath = path.copy()
            bestPathLen = len(path)
    else:
        if is_safe(row, col + 1):
            path.append((row, col + 1))
            find(row, col + 1)
        
        if is_safe(row - 1, col):
            path.append((row - 1, col))
            find(row - 1, col)
    
        if is_safe(row + 1, col):
            path.append((row + 1, col))
            find(row + 1, col)

        if is_safe(row, col - 1):
            path.append((row, col - 1))
            find(row, col - 1)
    del path[-1]

def is_safe(row, col):
    try:
        if land[row][col] == -1 or seen(row, col) or row == -1 or col == -1: return False
        else: return True
    except IndexError:
        return False

def seen(row, col):
    for i in range(len(path)):
        if path[i][0] == row and path[i][1] == col:
            return True
    return False

clear_the_map()

shortest_path()

print(bestPathLen)
for i in range(len(bestPath)):
    print(bestPath[i])