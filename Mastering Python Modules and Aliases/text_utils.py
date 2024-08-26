def reverse_string(inp):
    out = ""
    for i in range(-1, -len(inp)-1, -1):
        out += inp[i]
    return out

def capitalize_string(s):
    return s.upper()
