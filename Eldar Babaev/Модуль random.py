from random import randint


# BEGIN (write your solution here)
def choice_from_range(text, start, finish):
    random_index = randint(start, finish)
    result = text[random_index]
    return result
# END
