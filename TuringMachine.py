# TRANSITION_TABLE = [
#     [[1, "Q1", "L"], [0, "Q0", "L"], [1, "Q1", "R"]],
#     [[None, "Q1", "R"], [None, "Q1", "R"], [None, "Q2", "L"]],
#     [[None, "Q3", "L"], [None, "Q3", "L"], [None, "Q3", None]],
#     [[1, "Q3", "L"], [0, "Q3", "L"], [1, "Q4", "R"]],
#     [[None, None, None], [None, None, None], [None, None, None]]
#     ]

TRANSITION_TABLE = [
    [[1, 1, "L"], [0, 0, "L"], [1, 1, "R"]],
    [[None, 1, "R"], [None, 1, "R"], [None, 2, "L"]],
    [[None, 3, "L"], [None, 3, "L"], [None, 3, None]],
    [[1, 3, "L"], [0, 3, "L"], [1, 4, "R"]],
    [[None, None, None], [None, None, None], [None, None, None]]
    ]

binary_number = "ε110ε"

current_state = 0
i = binary_number
# for i in range(len(binary_number), -1, -1):
    current_char = binary_number[i]
    TRANSITION_TABLE[current_state]
    next_state =
