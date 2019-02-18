import sys


def shift_letter(s, n):
    begin = ord('A')
    relative_pos = ord(s) - begin
    relative_pos = (relative_pos + n) % 26
    absolute_pos = relative_pos + begin
    return chr(absolute_pos)


def enigma_code(oper: str, text: str, shit: int, rotors: list) -> str:
    # text only uppercase letters (A-Z)
    output = ""
    # print("input char:{}".format(text), file=sys.stderr)
    start = ord('A')

    if oper == 'ENCODE':
        for index, c in enumerate(text):
            new_char = shift_letter(c, shit + index)
            # print("new_char:{}".format(new_char), file=sys.stderr)
            for rotor in rotors:
                new_char_pos = ord(new_char) - start
                new_char = rotor[new_char_pos]
                # print("rotor:{}".format(rotor), file=sys.stderr)
                # print("char:{}".format(new_char), file=sys.stderr)
            output += new_char
    else:
        for index, c in enumerate(text):
            new_char = c
            for rotor in reversed(rotors):
                char_pos = rotor.index(new_char)
                new_char = chr(char_pos + start)
                # print("rotor:{}".format(rotor), file=sys.stderr)
                # print("char:{}".format(new_char), file=sys.stderr)
            output += shift_letter(new_char, -(shit + index))

    return output

# rotors = []
# output = ""
# operation = input()
# pseudo_random_number = int(input())
# for i in range(3):
#    rotors.append(input())
# msg = input()

operation = 'ENCODE'
pseudo_random_number = 7
rotors = ["BDFHJLCPRTXVZNYEIWGAKMUSQO",
         "AJDKSIRUXBLHWTMCQGZNPYFVOE",
         "EKMFLGDQVZNTOWYHXUSPAIBRCJ"]
msg = "WEATHERREPORTWINDYTODAY"

# operation = 'DECODE'
# pseudo_random_number = 9
# rotors = ["BDFHJLCPRTXVZNYEIWGAKMUSQO",
#           "AJDKSIRUXBLHWTMCQGZNPYFVOE",
#           "EKMFLGDQVZNTOWYHXUSPAIBRCJ"]
# msg = "PQSACVVTOISXFXCIAMQEM"

output = enigma_code(operation, msg, pseudo_random_number, rotors)
print(output)
