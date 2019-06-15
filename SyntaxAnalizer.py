from collections import OrderedDict

print("Analizator składniowy")

productions = OrderedDict([
    ("S", [list("W;Z")]),
    ("Z", [list("W;Z"), list("ε")]),
    ("W", [list("P"), list("POW")]),
    ("P", [list("R"), list("(W)")]),
    ("R", [list("L"), list("L.L")]),
    ("L", [list("C"), list("CL")]),
    ("C",
     [list("0"), list("1"), list("2"), list("3"), list("4"), list("5"), list("6"), list("7"), list("8"), list("9")]),
    ("O", [list("*"), list(":"), list("+"), list("-"), list("^")])
])

terminals = list(";().0123456789*,+-^ε:")

class IncorrectGrammarException(Exception):
   """Raised when the grammar is incorrect"""
   pass

firsts = OrderedDict()
first_rule_checks = OrderedDict()
type_of_transforms = OrderedDict()
follows = OrderedDict()
second_rule_checks = OrderedDict()


def print_ordered_dict(name, dict):
    print(name + ":")
    [print(x, ": ", dict[x]) for x in dict]


def first_of(name):
    if name in terminals:
        return name
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
    productions[name] = [[repeatable_char, name + "'"]]
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
    return list(nexts)


def check_second_rule(name):
    has_empty_sign = False
    for exp in productions[name]:
        if "ε" in exp:
            has_empty_sign = True
    if has_empty_sign:
        print("Checking second rule for", name, ":", productions[name])
        local_firsts = firsts[name].copy()
        local_follows = follows[name].copy()

        if "ε" in local_firsts: local_firsts.remove("ε")
        if "ε" in local_follows: local_follows.remove("ε")

        return set(local_firsts).isdisjoint(local_follows)
    else:
        return True


print_ordered_dict("Productions", productions)

[firsts.update({name: first_of(name)}) for name in productions]
print_ordered_dict("Firsts", firsts)

[first_rule_checks.update({final_expression: check_first_rule(productions[final_expression])}) for final_expression in
 productions]
print_ordered_dict("First rule", first_rule_checks)

# [follows.update({name: follow_of(name)}) for name in productions]

[refactor(name) for name in first_rule_checks if first_rule_checks[name] == False]
print_ordered_dict("Productions after transforms", productions)

[firsts.update({name: first_of(name)}) for name in productions]
print_ordered_dict("Firsts", firsts)

[first_rule_checks.update({final_expression: check_first_rule(productions[final_expression])}) for final_expression in
 productions]
print_ordered_dict("First rule", first_rule_checks)

[follows.update({name: follow_of(name)}) for name in productions]
print_ordered_dict("\nFollows", follows)

print()
[second_rule_checks.update({name: check_second_rule(name)}) for name in productions]
print_ordered_dict("Second rule", second_rule_checks)

counter = 0
exp_build = ""
word_to_check = "(1.2*3)+5-(23.4+3)^3;8:13;"
# word_to_check = "(3)"


def analize_syntax(exp, is_mandatory=False):
    global exp_build, word_to_check
    # print("Exp = ", exp)

    result = True

    for word in exp:
        char_to_check = word_to_check[analize_syntax.counter] if analize_syntax.counter < len(word_to_check) else "ε"
        if word in terminals and word == char_to_check:
            analize_syntax.counter += 1
            if word != "ε":
                exp_build += word
            # print(exp_build)
        elif not isinstance(word, list) and word in productions and char_to_check in first_of(word):
            # if :
                analize_syntax(productions[word])
        elif isinstance(word, list) and char_to_check in first_of(word[0]):
            # for char in word:
            is_valid = analize_syntax(word, True)
            if not is_valid:
                raise IncorrectGrammarException
        elif is_mandatory and (word in terminals or ["ε"] not in productions[word]):
            result = False
            # print(word, "not found")

    return result


analize_syntax.counter = 0

is_correct = True
try:
    analize_syntax(productions["S"])
except IncorrectGrammarException:
    is_correct = False
    print("IncorrectGrammarException")

print("exp build = ", exp_build)

if exp_build != word_to_check:
    is_correct = False

if is_correct:
    print("\nSłowo:", word_to_check, "zgode z gramatyką")
else:
    print("\nSłowo:", word_to_check, "niezgodne z gramatyką")
