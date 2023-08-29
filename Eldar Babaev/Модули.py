from symbols import is_vowel
def count_vowels(text: str) -> int:
    result = 0
    for iterat in text:
        if is_vowel(iterat.lower()):
            result += 1
    return result