def filter_string(string: str, symbol: str) -> str:
    out = ""
    for iterat in range(len(string)):
        if not (string[iterat].lower() == symbol.lower()):
            out += string[iterat]
    if out[0] == " ":
        out = out[1:]
    if out[len(out) - 1] == " ":
        out = out[:-1]
    return out