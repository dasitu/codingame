import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mt_mapping = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mt_mapping[ext.lower()] = mt
print("mt_mapping:{}".format(mt_mapping), file=sys.stderr)

for i in range(q):
    fname = input()  # One file name per line.
    ext = fname.split('.')
    ext_name = ""
    if len(ext) > 1:
        ext_name = ext[-1].lower()

    print("fname:{}".format(fname), file=sys.stderr)
    print("ext:{}".format(ext), file=sys.stderr)
    print("ext_name:{}".format(ext_name), file=sys.stderr)

    if ext_name in mt_mapping.keys():
        print(mt_mapping[ext_name])
    else:
        print("UNKNOWN")