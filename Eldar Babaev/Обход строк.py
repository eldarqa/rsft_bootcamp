def my_substr(string, length):
    i = 0
    result = ''
    while i < length:
        result = result + string[i]
        i += 1
    return result