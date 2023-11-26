def to_weird_case(words):
    word_list = words.split()
    ammended_list = []
    for word in word_list:
        letters = list(word)
        for letter in range(len(letters)):
            if letter % 2 == 0:
                letters[letter] = letters[letter].upper()
            else:
                letters[letter] = letters[letter].lower()
        word_joined = "".join(letters)
        ammended_list.append(word_joined)
    output = " ".join(ammended_list)
    print(output)


to_weird_case("THIs iS a TEST")
