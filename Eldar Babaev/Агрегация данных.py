def join_numbers_from_range(start, finish):
    i = start
    result = str(start)
    while i < finish:
        i = i + 1
        result = result + str(i)
    return result
