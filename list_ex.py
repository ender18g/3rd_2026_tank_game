number_matrix = [
        [ 1, 0, 0, 0, 0],
        [ 0, 1, 0, 0, 0],
        [ 0, 0, 1, 0, 0],
        [ 0, 0, 0, 1, 0],
        [ 0, 0, 0, 0, 1],        
    ]

areas = ['water', 'dirt']


for y in range(len(number_matrix)):
    for x in range(len(number_matrix[y])):
        print(f'{x},{y} = {number_matrix[y][x]} = {areas[number_matrix[y][x]]}')
        
