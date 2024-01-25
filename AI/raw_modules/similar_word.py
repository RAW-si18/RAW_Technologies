# Updated 23/1/24

from difflib import get_close_matches

def match_word_func(word: str, word_list: list) -> list:
    matches = get_close_matches(word, word_list)
    return matches