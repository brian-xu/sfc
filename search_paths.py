import itertools
import heapq

top_l = 0
top_r = 1
bottom_l = 2
bottom_r = 3

ordered_z = [
    [0, 0],
    [1, 0],
    [2, 0],
    [2, 1],
    [1, 1],
    [0, 1],
    [0, 2],
    [1, 2],
    [2, 2],
]
ordered_g = [
    [0, 0],
    [1, 0],
    [2, 0],
    [2, 1],
    [2, 2],
    [1, 2],
    [1, 1],
    [0, 1],
    [0, 2],
]


def grid(columns, rows):
    dims = []
    for height in rows:
        row = []
        for width in columns:
            row.append([width, height])
        dims.append(row)
    return dims


def sort_solutions(solutions):
    heap = []
    for sol in solutions:
        score = 0
        for dir in sol:
            if dir[0] == "s":
                score += 1
        heapq.heappush(heap, [score, sol])
    minscore = heap[0][0]
    res = []
    while heap and heap[0][0] == minscore:
        res.append(heapq.heappop(heap))
    return res


def search(even_columns, even_rows):
    column_dims = [2] * even_columns + [3] * (3 - even_columns)
    row_dims = [2] * even_rows + [3] * (3 - even_rows)
    columns = set(itertools.permutations(column_dims))
    rows = set(itertools.permutations(row_dims))
    res = []
    for column in columns:
        for row in rows:
            curve = grid(column, row)
            solutions_g = solve_g(curve, top_l, 0)[1]
            solutions_z = solve_z(curve, top_l, 0)[1]
            res.append([[column, row], {"g": solutions_g, "z": solutions_z}])
    return res


def solve_g(curve, corner, i):
    if i == 9:
        return True, [["end"]]
    solutions = []
    subsection = curve[ordered_g[i][0]][ordered_g[i][1]]
    if i == 0:
        if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
            viable, paths = solve_g(curve, top_r, i + 1)
            if viable:
                for path in paths:
                    solutions.append(["d_neg"] + path)
        if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
            viable, paths = solve_g(curve, top_l, i + 1)
            if viable:
                for path in paths:
                    solutions.append(["s_3_r"] + path)
    if i == 1:
        if corner == top_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_g(curve, top_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_neg"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_g(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_3_r"] + path)
        elif corner == top_r:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_g(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_pos_r"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_g(curve, top_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_1"] + path)
    if i == 2:
        if corner == top_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_g(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_neg"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [1, 0]:
                viable, paths = solve_g(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_0"] + path)
        elif corner == top_r:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_g(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_1"] + path)
    if i == 3:
        if corner == top_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_g(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_neg"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [1, 0]:
                viable, paths = solve_g(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_0"] + path)
        elif corner == bottom_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_g(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_pos"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [1, 0]:
                viable, paths = solve_g(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_2_r"] + path)
    if i == 4:
        if corner == top_l:
            if [subsection[0] % 2, subsection[1] % 2] != [1, 0]:
                viable, paths = solve_g(curve, bottom_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_0"] + path)
        elif corner == bottom_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_g(curve, bottom_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_pos"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_g(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_3"] + path)
    if i == 5:
        if corner == bottom_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_g(curve, top_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_3"] + path)
        elif corner == bottom_r:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_g(curve, top_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_neg_r"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [1, 0]:
                viable, paths = solve_g(curve, bottom_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_2"] + path)
    if i == 6:
        if corner == top_r:
            if [subsection[0] % 2, subsection[1] % 2] != [1, 0]:
                viable, paths = solve_g(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_0_r"] + path)
        elif corner == bottom_r:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_g(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_neg_r"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_g(curve, bottom_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_1_r"] + path)
    if i == 7:
        if corner == bottom_r:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_g(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_1_r"] + path)
        elif corner == bottom_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_g(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_pos"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [1, 0]:
                viable, paths = solve_g(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_2_r"] + path)
    if i == 8:
        if corner == top_l:
            if [subsection[0] % 2, subsection[1] % 2] != [1, 0]:
                viable, paths = solve_g(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_0"] + path)
        elif corner == bottom_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_g(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_pos"] + path)
    return len(solutions) > 0, solutions


def solve_z(curve, corner, i):
    if i == 9:
        return True, [["end"]]
    solutions = []
    subsection = curve[ordered_z[i][0]][ordered_z[i][1]]
    if i == 0:
        if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
            viable, paths = solve_z(curve, top_r, i + 1)
            if viable:
                for path in paths:
                    solutions.append(["d_neg"] + path)
        if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
            viable, paths = solve_z(curve, top_l, i + 1)
            if viable:
                for path in paths:
                    solutions.append(["s_3_r"] + path)
    if i == 1:
        if corner == top_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_z(curve, top_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_neg"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_z(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_3_r"] + path)
        elif corner == top_r:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_z(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_pos_r"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_z(curve, top_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_1"] + path)
    if i == 2:
        if corner == top_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_z(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_neg"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [1, 0]:
                viable, paths = solve_z(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_0"] + path)
        elif corner == top_r:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_z(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_1"] + path)
    if i == 3:
        if corner == top_l:
            if [subsection[0] % 2, subsection[1] % 2] != [1, 0]:
                viable, paths = solve_z(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_0"] + path)
        elif corner == bottom_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_z(curve, bottom_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_pos"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_z(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_3"] + path)
    if i == 4:
        if corner == bottom_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_z(curve, bottom_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_pos"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_z(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_3"] + path)
        elif corner == bottom_r:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_z(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_neg_r"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_z(curve, bottom_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_3"] + path)
    if i == 5:
        if corner == bottom_r:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_z(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_1_r"] + path)
        elif corner == bottom_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_z(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_pos"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [1, 0]:
                viable, paths = solve_z(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_2_r"] + path)
    if i == 6:
        if corner == bottom_l:
            if [subsection[0] % 2, subsection[1] % 2] != [1, 0]:
                viable, paths = solve_z(curve, top_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_2_r"] + path)
        elif corner == top_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_z(curve, top_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_neg"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_z(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_3_r"] + path)
    if i == 7:
        if corner == top_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_z(curve, top_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_neg"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_z(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_3_r"] + path)
        elif corner == top_r:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_z(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_pos_r"] + path)
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_z(curve, top_r, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_1"] + path)
    if i == 8:
        if corner == top_r:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 1]:
                viable, paths = solve_z(curve, bottom_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["s_1"] + path)
        elif corner == top_l:
            if [subsection[0] % 2, subsection[1] % 2] != [0, 0]:
                viable, paths = solve_z(curve, top_l, i + 1)
                if viable:
                    for path in paths:
                        solutions.append(["d_neg"] + path)
    return len(solutions) > 0, solutions


perms = []

for c in range(4):
    for r in range(4):
        print(c, r)
        for ordering, solution in search(c, r):
            print(ordering)
            if solution["g"]:
                print("G:", sort_solutions(solution["g"]))
                perms.append(len(sort_solutions(solution["g"])))
                print(len(sort_solutions(solution["g"])))
            if solution["z"]:
                print("Z:", sort_solutions(solution["z"]))
                perms.append(len(sort_solutions(solution["z"])))
                print(len(sort_solutions(solution["z"])))
print(perms)
