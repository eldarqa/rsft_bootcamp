def has_char(string, letter):
    index = 0
    result = False
    while index < len(string):
        if letter.lower() == string[index].lower():
            result = True
        index += 1
    return result