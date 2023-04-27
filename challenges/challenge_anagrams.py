# Agradecimentos a colega de turma: Aline

def quick_sort(letters, start, end):
    if start < end:
        p = partition(letters, start, end)
        quick_sort(letters, start, p - 1)
        quick_sort(letters, p + 1, end)


def partition(letters, start, end):
    pivot = letters[end]
    delimiter = start - 1

    for index in range(start, end):
        if letters[index] <= pivot:
            delimiter = delimiter + 1
            letters[index], letters[delimiter] = (
                letters[delimiter],
                letters[index],
            )
    letters[delimiter + 1], letters[end] = letters[end], letters[delimiter + 1]
    return delimiter + 1


def quick_sort_word(word):
    letters = list(word.lower())
    start = 0
    end = len(letters) - 1
    quick_sort(letters, start, end)
    return "".join(letters)


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return (quick_sort_word(first_string),
                quick_sort_word(second_string), False)
    equal = quick_sort_word(first_string) == quick_sort_word(second_string)
    return (quick_sort_word(first_string),
            quick_sort_word(second_string), equal)
