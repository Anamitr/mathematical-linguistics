from collections import OrderedDict

TRANSITION_TABLE = [
    [[1, 1, None], [0, 0, "L"], [1, 1, "R"]],
    [[None, 1, "R"], [None, 1, "R"], [None, 2, "L"]],
    [[None, 3, "L"], [None, 3, "L"], [None, 3, None]],
    [[1, 4, "L"], [0, 3, "L"], [1, 4, "R"]],
    [[None, None, None], [None, None, None], [None, None, None]]
    ]

MOVES = OrderedDict([
    ("L", -1),
    ("R", 1)
])

END_STATES = [4]

binary_number = "εε1010101010ε"

current_state = 0
i = len(binary_number) - 2

all_states = []


def make_move(move):
    global i, binary_number, current_state
    char_to_write = move[0]
    if char_to_write is not None:
        binary_number = "".join((binary_number[:i], str(char_to_write), binary_number[(i+1):]))
    current_state = move[1]
    if move[2] is not None:
        i += MOVES[move[2]]
    pass


while True:
    # print("i = ", i, ", current state = ", current_state, ", binary number = ", binary_number)
    all_states.append(current_state)
    current_char = binary_number[i]
    if current_char == "ε":
        current_char = 2
    else:
        current_char = int(current_char)

    move = TRANSITION_TABLE[current_state][current_char]
    # print(move)
    make_move(move)

    if current_state in END_STATES:
        break

print("All states:", all_states)
print("Number after transform:", binary_number)
