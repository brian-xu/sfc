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


def gen_curve(w, h, d=None):
    if w == 1:
        if h == 1:
            return True
        if d[2] in ["0", "2"]:
            return False
        else:
            return True
    if h == 1:
        if d[2] in ["1", "3"]:
            return False
        else:
            return True
    if w == 2:
        if h % 2 == 0:
            return d[0] == "s"
        if h % 2 == 1:
            return d[2] not in ["1", "3"]
    if h == 2:
        if w % 2 == 0:
            return d[0] == "s"
        if w % 2 == 1:
            return d[2] not in ["0", "2"]
    # w_parity = number of even-width columns
    w_div = w // 3
    w_mod = w % 3
    if w_div % 2 == 0:
        w_parity = 3 - w_mod
    else:
        w_parity = w_mod
    h_div = h // 3
    h_mod = h % 3
    if h_div % 2 == 0:
        h_parity = 3 - h_mod
    else:
        h_parity = h_mod
    offset, sol = curve_map[w_parity][h_parity]
    if d:
        if d[0] == "d" and "Z" not in sol:
            return False
        if d[0] == "s" and "G" not in sol:
            return False
    w_offset, h_offset = offset
    if w_div % 2 == 1:
        if w_mod == 0:
            w_dim = w_offset + w_div - 1
        else:
            w_dim = (w_div + 1) - w_offset
    else:
        w_dim = w_offset + w_div
    if h_div % 2 == 1:
        if h_mod == 0:
            h_dim = h_offset + h_div - 1
        else:
            h_dim = (h_div + 1) - h_offset
    else:
        h_dim = h_offset + h_div
    subsections = grid(w_dim, h_dim)
    if not d or d[0] == "d":
        for i in range(9):
            if not gen_curve(*subsections[ordered_z[i][0]][ordered_z[i][1]], sol["Z"][i]):
                print(subsections[ordered_z[i][0]][ordered_z[i][1]], sol["Z"][i])
                return False
    if not d or d[0] == "s":
        for i in range(9):
            if not gen_curve(*subsections[ordered_g[i][0]][ordered_g[i][1]], sol["G"][i]):
                print(subsections[ordered_g[i][0]][ordered_g[i][1]], sol["G"][i])
                return False
    return True
