import numpy as np
import functools
from typing import List
from copy import deepcopy


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


def grid(columns: List[int], rows: List[int]) -> List[List[int]]:
    dims = []
    for height in rows:
        row = []
        for width in columns:
            row.append([width, height])
        dims.append(row)
    return dims
