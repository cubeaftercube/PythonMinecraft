import re


def parse_minecraft_data(output_str: str):
    """
    Parses Minecraft command output (SNBT format) into a Python dictionary.
    Handles typed arrays (e.g., [I; ...]), NBT numeric suffixes (b, s, l, f, d),
    and nested objects/arrays.
    """
    # Strip the command response prefix (e.g., "aaabeats has the following entity data: ")
    idx = output_str.find("{")
    if idx != -1:
        data_str = output_str[idx:]
    else:
        return {}

    pos = 0

    def skip_whitespace():
        nonlocal pos
        while pos < len(data_str) and data_str[pos].isspace():
            pos += 1

    def is_int(s):
        return bool(re.match(r'^-?\d+$', s))

    def is_float(s):
        return bool(re.match(r'^-?\d+(\.\d+)?([eE][-+]?\d+)?$', s))

    def parse_value():
        nonlocal pos
        skip_whitespace()
        if pos >= len(data_str):
            return None

        char = data_str[pos]
        if char == '{':
            return parse_object()
        elif char == '[':
            return parse_array()
        elif char == '"':
            return parse_string()
        else:
            return parse_primitive()

    def parse_object():
        nonlocal pos
        pos += 1  # skip '{'
        obj = {}
        skip_whitespace()
        if pos < len(data_str) and data_str[pos] == '}':
            pos += 1
            return obj

        while True:
            skip_whitespace()
            if pos < len(data_str) and data_str[pos] == '}':
                pos += 1
                break

            key_start = pos
            while pos < len(data_str) and data_str[pos] not in ':\n\r ':
                pos += 1
            key = data_str[key_start:pos]

            # Handle quoted keys safely
            if key.startswith('"') and key.endswith('"') and len(key) >= 2:
                key = key[1:-1]

            skip_whitespace()
            if pos < len(data_str) and data_str[pos] == ':':
                pos += 1  # skip ':'
            else:
                break

            value = parse_value()
            obj[key] = value

            skip_whitespace()
            if pos < len(data_str) and data_str[pos] == ',':
                pos += 1  # skip ','
                continue
            elif pos < len(data_str) and data_str[pos] == '}':
                pos += 1
                break
            else:
                break
        return obj

    def parse_array():
        nonlocal pos
        pos += 1  # skip '['
        skip_whitespace()

        # Check for typed arrays like [I; 1, 2, 3] (Integers, Bytes, Longs)
        if pos + 1 < len(data_str) and data_str[pos + 1] == ';' and data_str[pos] in 'IBL':
            pos += 2  # skip type and ';'
            skip_whitespace()
            if pos < len(data_str) and data_str[pos] == ']':
                pos += 1
                return []

        arr = []
        if pos < len(data_str) and data_str[pos] == ']':
            pos += 1
            return arr

        while True:
            skip_whitespace()
            if pos < len(data_str) and data_str[pos] == ']':
                pos += 1
                break

            val = parse_value()
            arr.append(val)

            skip_whitespace()
            if pos < len(data_str) and data_str[pos] == ',':
                pos += 1
                continue
            elif pos < len(data_str) and data_str[pos] == ']':
                pos += 1
                break
            else:
                break
        return arr

    def parse_string():
        nonlocal pos
        pos += 1  # skip '"'
        start = pos
        while pos < len(data_str) and data_str[pos] != '"':
            if data_str[pos] == '\\':
                pos += 1  # skip escape char
            pos += 1
        res = data_str[start:pos]
        if pos < len(data_str):
            pos += 1  # skip closing '"'
        return res

    def parse_primitive():
        nonlocal pos
        start = pos
        while pos < len(data_str) and data_str[pos] not in ',}]\n\r ':
            pos += 1
        val = data_str[start:pos]

        # NBT typed suffix parsing
        if val.endswith('b') and is_int(val[:-1]):
            return int(val[:-1])
        elif val.endswith('s') and is_int(val[:-1]):
            return int(val[:-1])
        elif val.endswith('l') and is_int(val[:-1]):
            return int(val[:-1])
        elif val.endswith('f') and is_float(val[:-1]):
            return float(val[:-1])
        elif val.endswith('d') and is_float(val[:-1]):
            return float(val[:-1])
        elif is_int(val):
            return int(val)
        elif is_float(val):
            return float(val)
        else:
            return val

    return parse_value()

