import re

REGEX = "^([-]*[0-9][0-9]*([+-/*^][-]*[0-9][0-9]*)*;)*$"
# REGEX = "^[([-]*[0-9][0-9]*([+-/*^][-]*[0-9][0-9]*)*)|([(][-]*[0-9][0-9]*([+-/*^][-]*[0-9][0-9]*)*;[)])];*$"

exp = "12+2*9;3*8^12-2/3;"
# exp = "(1.2*3)+5-(23.4+3)^3;"

pattern = re.compile(REGEX)
result = pattern.match(exp)

print(result)
if result is not None:
    print("Wyrażenie jest zgodne z gramatyką")
else:
    print("Wyrażenie jest niezgodne z gramatyką")
