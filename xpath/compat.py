import sys


PY2 = sys.version_info[0] == 2

if PY2:
    str_encode = str.decode
    string_types = (str, unicode)
else:
    str_encode = str.encode
    string_types = (str, bytes)
