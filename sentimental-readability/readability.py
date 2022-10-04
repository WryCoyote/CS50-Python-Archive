# TODO

import cs50


def main():

    words = cs50.get_string("Text: ")
    letterCount = count_letters(words)
    wordCount = count_words(words)
    scentanceCount = count_scentances(words)

    L = letterCount / wordCount * 100
    S = scentanceCount / wordCount * 100

    index = 0.0588 * L - 0.296 * S - 15.8
    # print("index check: ", index)
    grade = int(round(index, 0))
    # print("grade check: ", grade)

    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print("Grade ", grade)


def count_letters(text):
    letters = 0
    for i in range(len(text)):
        if text[i].isalpha():
            letters = letters + 1

    # print("letter check: ", letters)
    return letters


def count_words(text):
    words = 1
    for i in range(len(text)):
        if text[i] == ' ':
            words = words + 1

    # print("word check: ", words)
    return words


def count_scentances(text):
    scentances = 0
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            scentances = scentances + 1

    # print("scentance check: ", scentances)
    return scentances


if __name__ == "__main__":
    main()