from collections import OrderedDict

print("Analizator składniowy")

productions = OrderedDict([
    ("S", ["W;Z"]),
    ("Z", ["W;Z", "ε"]),
    ("W", ["P", "POW"]),
    ("P", ["R", "(W)"]),
    ("R", ["L", "L.L"]),
    ("L", ["C", "CL"]),
    ("C", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]),
    ("O", ["*", ",", "+", "-", "^"])
])

terminals = list(";().0123456789*,+-^ε")

firsts = OrderedDict()
first_rule_checks = OrderedDict()
type_of_transforms = OrderedDict()


def print_ordered_dict(name, dict):
    print(name + ":")
    [print(x, ": ", dict[x]) for x in dict]


def first_of(name):
    result = []
    expression = productions[name]
    for word in expression:
        first = word[0]
        if first in terminals and first not in result:
            result.append(first)
        elif first == name:
            continue
        elif first in productions:
            result += (first_of(first))
            result = list(dict.fromkeys(result))
    return result


def check_first_rule(expression):
    terminals = []
    left_words = []
    for unit in expression:
        left_words.append(unit[0])

    for word in left_words:
        if word in terminals:
            terminals.append(word)
        elif word in productions:
            terminals += (first_of(word))
    return len(terminals) == len(set(terminals))


def refactor(name):
    expression = productions[name]
    repeatable_char = expression[0][0]
    productions[name] = [repeatable_char + name + "'"]
    productions[name + "'"] = [word[1:] if word[1:] != "" else "ε" for word in expression]


print_ordered_dict("Productions", productions)

[firsts.update({name: first_of(name)}) for name in productions]
print_ordered_dict("Firsts", firsts)

[first_rule_checks.update({exp: check_first_rule(productions[exp])}) for exp in productions]
print_ordered_dict("First rule", first_rule_checks)

[refactor(name) for name in first_rule_checks if first_rule_checks[name] == False]
print_ordered_dict("Productions after transforms", productions)
