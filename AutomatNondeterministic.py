print('Automat niedeterministyczny')

data_from_file = str
data = []

with open('dane', 'r') as file:
    data_from_file = file.read().replace('\n', '')
data_from_file = data_from_file.split('#')
for s in data_from_file:
    s = list(s)
    data.append(s)

transition_array = [[[0, 1], [0, 3], [0, 5], [0, 7], [0, 9], [0, 11], [0, 13], [0, 15], [0, 17], [0, 19]],
                    [2, None, None, None, None, None, None, None, None, None, None],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [None, 4, None, None, None, None, None, None, None, None, None],
                    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    [None, None, 6, None, None, None, None, None, None, None, None],
                    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
                    [None, None, None, 8, None, None, None, None, None, None, None],
                    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                    [None, None, None, None, 10, None, None, None, None, None, None],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                    [None, None, None, None, None, 12, None, None, None, None, None],
                    [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
                    [None, None, None, None, None, None, 14, None, None, None, None],
                    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
                    [None, None, None, None, None, None, None, 16, None, None, None],
                    [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16],
                    [None, None, None, None, None, None, None, None, 18, None, None],
                    [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18],
                    [None, None, None, None, None, None, None, None, None, 20, None],
                    [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                    [None, None, None, None, None, None, None, None, None, None, 22],
                    [22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22],
                    ]

input_map = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "a": 5,
    "b": 6,
    "c": 7,
    "e": 8,
    "f": 9,
}

results = [None, None, "cyfry 0", None, "cyfry 1", None, "cyfry 2", None, "cyfry 3", None, "cyfry 4", None, "litery a", None, "litery b",
           None, "litery c", None, "litery e", None, "litery f"]

print(data_from_file)
print(data)

for i, data_row in enumerate(data):
    print("Ciąg nr " + str(i) + ":")
    states = [0]
    new_states = states.copy()

    # Przejdź przez wszystkie stany
    for character in data_row:
        print(states, " -> ", character, ":")
        input_value = input_map.get(character, None)

        if input_value is not None:
            for state in states:
                next_states = transition_array[state][input_value]
                if not isinstance(next_states, list):
                    next_states = [next_states]
                new_states.remove(state)
                new_states += next_states  # list(set(next_states) - set(new_states))
                new_states = [x for x in new_states if x is not None]
        states = new_states.copy()

    print(states)

    # Wydrukuj wyniki
    for state in states:
        result = results[state]
        if result is not None:
            print("Wystąpiło powtórzenie wśród " + str(result))
