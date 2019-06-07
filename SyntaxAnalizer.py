from collections import OrderedDict

print("Analizator składniowy")

# productions = OrderedDict([
#     ("S", ["W;Z"]),
#     ("Z", ["W;Z", "ε"]),
#     ("W", ["P", "POW"]),
#     ("P", ["R", "(W)"]),
#     ("R", ["L", "L.L"]),
#     ("L", ["C", "CL"]),
#     ("C", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]),
#     ("O", ["*", ",", "+", "-", "^"])
# ])

productions = OrderedDict([
    ("S", [list("W;Z")]),
    ("Z", [list("W;Z"), list("ε")]),
    ("W", [list("P"), list("POW")]),
    ("P", [list("R"), list("(W)")]),
    ("R", [list("L"), list("L.L")]),
    ("L", [list("C"), list("CL")]),
    ("C", [list("0"), list("1"), list("2"), list("3"), list("4"), list("5"), list("6"), list("7"), list("8"), list("9")]),
    ("O", [list("*"), list("),"), list("+"), list("-"), list("^")])
])

terminals = list(";().0123456789*,+-^ε")

firsts = OrderedDict()
first_rule_checks = OrderedDict()
type_of_transforms = OrderedDict()
follows = OrderedDict()
second_rule_checks = OrderedDict()


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
    productions[name] = [[repeatable_char,  name + "'"]]
    productions[name + "'"] = [word[1:] if word[1:] != [] else ["ε"] for word in expression]

def follow_of(name, called_by_prod=None):
    nexts = set([])
    for prod in productions:
        for exp in productions[prod]:
            indices = [i for i, x in enumerate(exp) if x == name]
            for index in indices:
                if index + 1 >= len(exp):
                    if prod != name and called_by_prod != prod:
                        nexts.update(follow_of(prod, name))
                else:
                    if exp[index + 1] in terminals:
                        nexts.update(exp[index + 1])
                    else:
                        nexts.update(first_of(exp[index + 1]))
    # print("Follow of", name, ":", nexts)
    return list(nexts)

def check_second_rule(name):
    result = False
    print(name, ": ", firsts[name])
    print (name, ": ", follows[name])
    return set(firsts[name]).isdisjoint(follows[name])

print_ordered_dict("Productions", productions)

[firsts.update({name: first_of(name)}) for name in productions]
print_ordered_dict("Firsts", firsts)

[first_rule_checks.update({exp: check_first_rule(productions[exp])}) for exp in productions]
print_ordered_dict("First rule", first_rule_checks)

# [follows.update({name: follow_of(name)}) for name in productions]

[refactor(name) for name in first_rule_checks if first_rule_checks[name] == False]
print_ordered_dict("Productions after transforms", productions)

[firsts.update({name: first_of(name)}) for name in productions]
print_ordered_dict("Firsts", firsts)

[first_rule_checks.update({exp: check_first_rule(productions[exp])}) for exp in productions]
print_ordered_dict("First rule", first_rule_checks)

[follows.update({name: follow_of(name)}) for name in productions]
print_ordered_dict("\nFollows", follows)

print()
[second_rule_checks.update({name: check_second_rule(name)}) for name in productions]
print_ordered_dict("Second rule", second_rule_checks)