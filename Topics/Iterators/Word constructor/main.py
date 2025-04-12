def word_constructor() -> None:
    result = ''
    word1 = input()
    word2 = input()
    list_of_chars1 = list(word1)
    list_of_chars2 = list(word2)
    for char1, char2 in zip(list_of_chars1, list_of_chars2):
        result += (char1 + char2)

    print(result)

word_constructor()
