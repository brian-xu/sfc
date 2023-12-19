import numpy as np

# curve_map[column width parity][row height parity]
curve_map = [
    [
        [
            [np.array([1, 1, 1]), np.array([1, 1, 1])],
            {
                "G": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "s_0",
                    "d_neg_r",
                    "s_0_r",
                    "d_pos",
                    "s_0",
                ],
                "Z": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "d_neg_r",
                    "d_pos",
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                ],
            },
        ],
        [
            [np.array([1, 1, 1]), np.array([1, 1, 0])],
            {
                "Z": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "d_neg_r",
                    "d_pos",
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                ]
            },
        ],
        [
            [np.array([1, 1, 1]), np.array([1, 0, 0])],
            {
                "Z": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "d_neg_r",
                    "d_pos",
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                ]
            },
        ],
        [
            [np.array([1, 1, 1]), np.array([0, 0, 0])],
            {
                "Z": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "d_neg_r",
                    "d_pos",
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                ]
            },
        ],
    ],
    [
        [
            [np.array([1, 1, 0]), np.array([1, 1, 1])],
            {
                "G": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "s_0",
                    "d_neg_r",
                    "s_0_r",
                    "d_pos",
                    "s_0",
                ],
                "Z": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "d_neg_r",
                    "d_pos",
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                ],
            },
        ],
        [
            [np.array([1, 1, 0]), np.array([1, 1, 0])],
            {
                "G": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "s_0",
                    "d_neg_r",
                    "s_0_r",
                    "d_pos",
                    "s_0",
                ]
            },
        ],
        [
            [np.array([1, 1, 0]), np.array([1, 0, 0])],
            {
                "G": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "s_0",
                    "s_2",
                    "d_neg_r",
                    "d_pos",
                    "s_0",
                ],
                "Z": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "d_neg_r",
                    "d_pos",
                    "d_neg",
                    "s_1",
                    "s_1",
                ],
            },
        ],
        [
            [np.array([1, 1, 0]), np.array([0, 0, 0])],
            {
                "G": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "s_0",
                    "s_2",
                    "d_neg_r",
                    "d_pos",
                    "s_0",
                ]
            },
        ],
    ],
    [
        [
            [np.array([1, 0, 0]), np.array([1, 1, 1])],
            {
                "G": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "s_0",
                    "d_neg_r",
                    "s_0_r",
                    "d_pos",
                    "s_0",
                ],
                "Z": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "d_neg_r",
                    "d_pos",
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                ],
            },
        ],
        [
            [np.array([1, 0, 0]), np.array([0, 1, 1])],
            {
                "Z": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "d_neg_r",
                    "s_2_r",
                    "s_2_r",
                    "d_pos_r",
                    "d_neg",
                ]
            },
        ],
        [
            [np.array([1, 0, 0]), np.array([1, 0, 0])],
            {
                "G": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "s_2_r",
                    "s_3",
                    "s_3",
                    "s_0_r",
                    "d_pos",
                    "s_0",
                ],
                "Z": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "s_3",
                    "s_3",
                    "d_pos",
                    "d_neg",
                    "s_1",
                    "s_1",
                ],
            },
        ],
        [
            [np.array([1, 0, 0]), np.array([0, 0, 0])],
            {
                "Z": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "s_3",
                    "s_3",
                    "s_2_r",
                    "s_2_r",
                    "s_1",
                    "s_1",
                ]
            },
        ],
    ],
    [
        [
            [np.array([0, 0, 0]), np.array([1, 1, 1])],
            {
                "G": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "s_0",
                    "d_neg_r",
                    "s_0_r",
                    "d_pos",
                    "s_0",
                ],
                "Z": [
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                    "d_pos",
                    "d_neg_r",
                    "d_pos",
                    "d_neg",
                    "d_pos_r",
                    "d_neg",
                ],
            },
        ],
        [
            [np.array([0, 0, 0]), np.array([1, 1, 0])],
            {
                "G": [
                    "d_neg",
                    "d_pos_r",
                    "s_0",
                    "s_0",
                    "s_0",
                    "d_neg_r",
                    "s_0_r",
                    "d_pos",
                    "s_0",
                ]
            },
        ],
        [
            [np.array([0, 0, 0]), np.array([1, 0, 0])],
            {
                "G": [
                    "d_neg",
                    "s_1",
                    "s_1",
                    "s_2_r",
                    "s_3",
                    "s_3",
                    "s_0_r",
                    "d_pos",
                    "s_0",
                ],
                "Z": [
                    "d_neg",
                    "s_1",
                    "s_1",
                    "s_3",
                    "s_3",
                    "d_pos",
                    "d_neg",
                    "s_1",
                    "s_1",
                ],
            },
        ],
        [
            [np.array([0, 0, 0]), np.array([0, 0, 0])],
            {
                "G": [
                    "s_3_r",
                    "s_3_r",
                    "s_0",
                    "s_0",
                    "s_0",
                    "s_2",
                    "s_1_r",
                    "s_1_r",
                    "s_0",
                ]
            },
        ],
    ],
]

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


def gen_curve(width, height, d):
    if width == 1:
        if height == 1:
            return [np.array([[0]]), False]
        if d in ["s_0", "s_0_r", "s_2", "s_2_r"]:
            return [np.array([]), False]
        if d in ["s_1", "s_3_r", "d_neg", "d_pos_r"]:
            return [np.array([[i] for i in range(height)]), False]
        if d in ["s_3", "s_1_r", "d_pos", "d_neg_r"]:
            return [np.array([[height-i-1] for i in range(height)]), False]
    if height == 1:
        if d in ["s_1", "s_1_r", "s_3", "s_3_r"]:
            return [np.array([]), False]
        if d in ["s_0", "s_2_r", "d_neg", "d_pos"]:
            return [np.array([[i for i in range(width)]]), False]
        if d in ["s_2", "s_0_r", "d_neg_r", "d_pos_r"]:
            return [np.array([[width-i-1 for i in range(width)]]), False]
    if width == 2:
        if height % 2 == 0:
            if d in ["d_neg", "d_neg_r", "d_pos", "d_pos_r"]:
                return [np.array([]), False]
            else:
                return [np.array([[i, 2*height-i-1] for i in range(height)]), True]
        if height % 2 == 1:
            if d in ["s_1", "s_1_r", "s_3", "s_3_r"]:
                return [np.array([]), False]
            if d in ["s_0", "s_0_r", "s_2", "s_2_r"]:
                return [np.array([[i, 2*height-i-1] for i in range(height)]), True]
            if d in ["d_neg", "d_neg_r"]:
                return [np.array([[2*i+1*(i%2), 2*i+1*(1-i%2)] for i in range(height)]), True]
            if d in ["d_pos", "d_pos_r"]:
                return [np.array([[2*i+1*(1-i%2), 2*i+1*(i%2)] for i in range(height)]), True]
    if height == 2:
        if width % 2 == 0:
            if d in ["d_neg", "d_neg_r", "d_pos", "d_pos_r"]:
                return [np.array([]), False]
            else:
                return [np.array([[i for i in range(width)], [2*width-i-1 for i in range(width)]]), True]
        if width % 2 == 1:
            if d in ["s_0", "s_0_r", "s_2", "s_2_r"]:
                return [np.array([]), False]
            if d in ["s_1", "s_1_r", "s_3", "s_3_r"]:
                return [np.array([[i, 2*height-i-1] for i in range(height)]), True]
            if d in ["d_neg", "d_neg_r"]:
                return [np.array([[i*2 + 1*(i%2) for i in range(width)], [i*2 + 1*(1-i%2) for i in range(width)]]), True]
            if d in ["d_pos", "d_pos_r"]:
                return [np.array([[i*2 + 1*(1-i%2) for i in range(width)], [i*2 + 1*(i%2) for i in range(width)]]), True]
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
            return [np.array([]), False]
        else:
            order = ordered_z
            solution = solution["Z"]
    if d[0] == "s":
        if "G" not in solution:
            return [np.array([]), False]
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
        subsection_direction = solution[n]
        curve_direction = subsection_direction
        subsection_width, subsection_height = subsections[i][j]
        if subsection_direction[2] in ["1", "3"]:
            if subsection_width > 2 and subsection_height > 2:
                subsection_width, subsection_height = subsection_height, subsection_width
                curve_direction = "s_0"
                if subsection_direction[-1] == "r":
                    curve_direction += "_r"
        if subsection_direction[2] == "p":
            if subsection_width > 2 and subsection_height > 2:
                subsection_width, subsection_height = subsection_height, subsection_width
                curve_direction = "d_neg"
                if subsection_direction[-1] == "r":
                    curve_direction += "_r"
        subsection, needs_rotation = gen_curve(subsection_width, subsection_height, curve_direction)
        if len(subsection) == 0:
            return [np.array([]), False]
        if needs_rotation:
            rotations = subsection_direction[2]
            if rotations == "p":
                subsection = np.rot90(subsection, k=1)
            if rotations.isnumeric():
                subsection = np.rot90(subsection, k=-int(rotations))
            if subsection_direction[-1] == "r":
                subsection = subsection.size-1-subsection
        res[i][j] = subsection
    prev = 0
    for n in range(9):
        i, j = order[n]
        res[i][j] += prev
        prev += res[i][j].size
    res = np.vstack([np.hstack(res[0]),np.hstack(res[1]),np.hstack(res[2])])
    return [res, True]

x, _ = gen_curve(9, 9,"s_0")
print(x)