import sys

message = "%"

bin_message = ""
for letter in message:
    bin_message += '{0:07b}'.format(ord(letter))
print("bin_message:{}".format(bin_message), file=sys.stderr)

mapping_result = []
pre_char = bin_message[0]
char_count = 1
for char in bin_message[1:]:
    if char == pre_char:
        char_count += 1
    else:
        mapping_result.append((pre_char, char_count))
        char_count = 1
    pre_char = char
mapping_result.append((pre_char, char_count))

print("mapping_result:{}".format(mapping_result), file=sys.stderr)

output = ""
for char, count in mapping_result:
    if char == "0":
        output += "00 "
    elif char == "1":
        output += "0 "
    output += "0" * count
    output += " "
print(output.rstrip())
