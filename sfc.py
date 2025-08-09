import numpy as np
from utils import curve_map, ordered_g, ordered_z, grid, lru_cache


@lru_cache(copy=True)
def gen_curve(width: int, height: int, d: str) -> np.array:
    if width == 0 or height == 0:
        return np.array([])
    if width == 1:
        if height == 1:
            return np.array([[0]])
        if d in ["s_0", "s_0_r", "s_2", "s_2_r"]:
            return np.array([])
        if d in ["s_1", "s_3_r", "d_neg", "d_pos_r"]:
            return np.array([[i] for i in range(height)])
        if d in ["s_3", "s_1_r", "d_pos", "d_neg_r"]:
            return np.array([[height - i - 1] for i in range(height)])
    if height == 1:
        if d in ["s_1", "s_1_r", "s_3", "s_3_r"]:
            return np.array([])
        if d in ["s_0", "s_2_r", "d_neg", "d_pos"]:
            return np.array([[i for i in range(width)]])
        if d in ["s_2", "s_0_r", "d_neg_r", "d_pos_r"]:
            return np.array([[width - i - 1 for i in range(width)]])
    if width == 2:
        if d == "s_0":
            return np.array([[i, 2 * height - i - 1] for i in range(height)])
        if d == "d_neg":
            if height % 2 == 0:
                return np.array([])
            else:
                return np.array(
                    [
                        [2 * i + 1 * (i % 2), 2 * i + 1 * (1 - i % 2)]
                        for i in range(height)
                    ]
                )
    if height == 2:
        if width % 2 == 0:
            if d == "d_neg":
                return np.array([])
            if d == "s_0":
                return np.array(
                    [
                        [2 * i + 1 * (i % 2), 2 * i + 1 * (1 - i % 2)]
                        for i in range(width)
                    ]
                ).T
        if width % 2 == 1:
            if d == "s_0":
                return np.array([])
            if d == "d_neg":
                return np.array(
                    [
                        [i * 2 + 1 * (i % 2) for i in range(width)],
                        [i * 2 + 1 * (1 - i % 2) for i in range(width)],
                    ]
                )
    # width_parity = number of even-width columns
    width_div = width // 3
    width_mod = width % 3
    if width_div % 2 == 0:
        width_parity = 3 - width_mod
    else:
        width_parity = width_mod
    height_div = height // 3
    height_mod = height % 3
    if height_div % 2 == 0:
        height_parity = 3 - height_mod
    else:
        height_parity = height_mod
    offset, solution = curve_map[width_parity][height_parity]
    if d[0] == "d":
        if "Z" not in solution:
            return np.array([])
        else:
            order = ordered_z
            solution = solution["Z"]
    if d[0] == "s":
        if "G" not in solution:
            return np.array([])
        else:
            order = ordered_g
            solution = solution["G"]
    width_offset, height_offset = offset
    if width_div % 2 == 1:
        if width_mod == 0:
            width_dim = width_offset + width_div - 1
        else:
            width_dim = (width_div + 1) - width_offset
    else:
        width_dim = width_offset + width_div
    if height_div % 2 == 1:
        if height_mod == 0:
            height_dim = height_offset + height_div - 1
        else:
            height_dim = (height_div + 1) - height_offset
    else:
        height_dim = height_offset + height_div
    subsections = grid(width_dim, height_dim)
    res = [[0 for _ in range(3)] for __ in range(3)]
    for n in range(9):
        i, j = order[n]
        sub_direction = solution[n]
        sub_width, sub_height = subsections[i][j]
        if sub_direction[2] in ["1", "3"] and sub_width > 1 and sub_height > 1:
            subsection = gen_curve(sub_height, sub_width, "s_0")
        elif sub_direction[2] in ["0", "2"] and sub_width > 1 and sub_height > 1:
            subsection = gen_curve(sub_width, sub_height, "s_0")
        elif sub_direction[2] == "p" and sub_width > 1 and sub_height > 1:
            subsection = gen_curve(sub_height, sub_width, "d_neg")
        else:
            subsection = gen_curve(sub_width, sub_height, sub_direction)
        if len(subsection) == 0:
            return np.array([])
        if sub_width > 1 and sub_height > 1:
            rotations = sub_direction[2]
            if rotations == "p":
                subsection = np.rot90(subsection, k=1)
            if rotations.isnumeric():
                subsection = np.rot90(subsection, k=-int(rotations))
            if sub_direction[-1] == "r":
                subsection = subsection.size - 1 - subsection
        res[i][j] = subsection
    prev = 0
    for n in range(9):
        i, j = order[n]
        res[i][j] += prev
        prev += res[i][j].size
    res = np.vstack([np.hstack(res[0]), np.hstack(res[1]), np.hstack(res[2])])
    return res
