# def check_if_recursive(name):
#     result = False
#     expression = not_terminals[name]
#     for word in expression:
#         first = word[0]
#         if first == name:
#             result = True
#             return result
#     return result
#
# def get_type_of_transform(name):
#     result = None
#     if check_if_recursive(name):
#         return TransformType.RECURSION
#
#     return name

# def transform

# for i in range(0, len(not_terminals)):
#     firsts.update({list(not_terminals.items())[i][0]: first_of(list(not_terminals.items())[i])})


# [type_of_transforms.update({name: get_type_of_transform(name)}) for name in not_terminals if first_rule_checks[name] is False]
# [print(x, ": ", type_of_transforms[x]) for x in type_of_transforms]

# print(list(first_rule_checks.items())[2][1])
#
# for i in range(0, len(not_terminals)):
#     if list(first_rule_checks.items())[i][1] is False:
#         check_type_of_transform(list(not_terminals.items())[i])
#         transform(not_terminals[i])