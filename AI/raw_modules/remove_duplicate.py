# Updated 23/1/24

def remove_duplicate_words(input_string: str) -> str:
    words = input_string.split(' ')
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    result_string = ' '.join(unique_words)
    return result_string
