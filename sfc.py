import numpy as np
import functools
from typing import List
from copy import deepcopy


# https://stackoverflow.com/questions/54909357/how-to-get-functools-lru-cache-to-return-new-instances
def lru_cache(maxsize=128, typed=False, copy=False):
    if not copy:
        return functools.lru_cache(maxsize, typed)

    def decorator(f):
        cached_func = functools.lru_cache(maxsize, typed)(f)

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            return deepcopy(cached_func(*args, **kwargs))

        return wrapper

    return decorator


# curve_map[column width parity][row height parity]
# curve_map[i] = [[parity offsets], [solution orientations]]
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

# order of grid subsections for z-type curve in d_neg orientation
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

# order of grid subsections for g-type curve in s_0 orientation
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


def grid(columns: List[int], rows: List[int]) -> List[List[int]]:
    dims = []
    for height in rows:
        row = []
        for width in columns:
            row.append([width, height])
        dims.append(row)
    return dims


@lru_cache(copy=True)
def gen_curve(width: int, height: int, d: str) -> [np.array, bool]:
    if width == 0 or height == 0:
        return [np.array([]), False]
    if width == 1:
        if height == 1:
            return [np.array([[0]]), False]
        if d in ["s_0", "s_0_r", "s_2", "s_2_r"]:
            return [np.array([]), False]
        if d in ["s_1", "s_3_r", "d_neg", "d_pos_r"]:
            return [np.array([[i] for i in range(height)]), False]
        if d in ["s_3", "s_1_r", "d_pos", "d_neg_r"]:
            return [np.array([[height - i - 1] for i in range(height)]), False]
    if height == 1:
        if d in ["s_1", "s_1_r", "s_3", "s_3_r"]:
            return [np.array([]), False]
        if d in ["s_0", "s_2_r", "d_neg", "d_pos"]:
            return [np.array([[i for i in range(width)]]), False]
        if d in ["s_2", "s_0_r", "d_neg_r", "d_pos_r"]:
            return [np.array([[width - i - 1 for i in range(width)]]), False]
    if width == 2:
        if height % 2 == 0:
            if d == "d_neg":
                return [np.array([]), False]
            if d == "s_0":
                return [
                    np.array([[i, 2 * height - i - 1] for i in range(height)]),
                    True,
                ]
        if height % 2 == 1:
            if d == "s_0":
                return [
                    np.array([[i, 2 * height - i - 1] for i in range(height)]),
                    True,
                ]
            if d == "d_neg":
                return [
                    np.array(
                        [
                            [2 * i + 1 * (i % 2), 2 * i + 1 * (1 - i % 2)]
                            for i in range(height)
                        ]
                    ),
                    True,
                ]
    if height == 2:
        if width % 2 == 0:
            if d == "d_neg":
                return [np.array([]), False]
            if d == "s_0":
                return [
                    np.array(
                        [
                            [2 * i + 1 * (i % 2), 2 * i + 1 * (1 - i % 2)]
                            for i in range(width)
                        ]
                    ).T,
                    True,
                ]
        if width % 2 == 1:
            if d == "s_0":
                return [np.array([]), False]
            if d == "d_neg":
                return [
                    np.array(
                        [
                            [i * 2 + 1 * (i % 2) for i in range(width)],
                            [i * 2 + 1 * (1 - i % 2) for i in range(width)],
                        ]
                    ),
                    True,
                ]
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
        sub_direction = solution[n]
        sub_width, sub_height = subsections[i][j]
        if sub_direction[2] in ["1", "3"] and sub_width > 1 and sub_height > 1:
            subsection, needs_rotation = gen_curve(sub_height, sub_width, "s_0")
        elif sub_direction[2] == "2" and sub_width > 1 and sub_height > 1:
            subsection, needs_rotation = gen_curve(sub_width, sub_height, "s_0")
        elif sub_direction[2] == "p" and sub_width > 1 and sub_height > 1:
            subsection, needs_rotation = gen_curve(sub_height, sub_width, "d_neg")
        else:
            subsection, needs_rotation = gen_curve(sub_width, sub_height, sub_direction)
        if len(subsection) == 0:
            return [np.array([]), False]
        if needs_rotation:
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
    return [res, True]
