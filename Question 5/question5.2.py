import numpy as np
from more_itertools import distinct_permutations


def sort_ball(red_count: int, blue_count: int, green_count: int,white_count: int,yellow_count: int):
    original = list()
    red_range = range(red_count)
    blue_range = range(blue_count)
    green_range = range(green_count)
    white_range = range(white_count)
    yellow_range = range(yellow_count)

    for i in blue_range:
        original.append("B")
    for i in red_range:
        original.append("R")
    for i in green_range:
        original.append("G")
    for i in white_range:
        original.append("W")
    for i in yellow_range:
        original.append("Y")

    return distinct_permutations(original)


def check(mat,L):
    penalty = 0
    for i in range(L):
        for j in range(L):
            if i-1>=0 and mat[i-1][j] == mat[i][j]:
                penalty += 1
            if i+1<3 and mat[i+1][j] == mat[i][j]:
                penalty += 1
            if j-1>=0 and mat[i][j-1] == mat[i][j]:
                penalty += 1
            if j+1<3 and mat[i][j+1] == mat[i][j]:
                penalty += 1

    return penalty


def main():
    L = 64
    i = 0
    min_penalty = float('inf')
    min_grid = []
    for sorted in sort_ball(139, 1451, 977, 1072, 457):
        i += 1
        print(i)
        # print(''.join(i))
        grid = np.array(sorted).reshape(L,L)
        # print(grid)
        penalty = check(grid,L)
        if min_penalty > penalty:
            min_penalty = penalty
            min_grid = []
            min_grid.append(grid)
        elif min_penalty == penalty:
            min_grid.append(grid)

    print(min_grid)

    for i in range(len(min_grid)):
        grid = min_grid[i].astype('str')
        with open('output_question_5_2.txt', 'a') as f:
            np.savetxt(f, grid, fmt='%s', header='', comments='',footer='\n' )
        f.close()



if __name__ == '__main__':
    main()