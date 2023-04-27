def is_anagram(first_string, second_string):
    if len(first_string) == 0 or len(second_string) == 0:
        return False

    str1 = first_string.lower()
    str2 = second_string.lower().reverse()

    return str1 == str2
