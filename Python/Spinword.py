

def spin_words(sentence):
    list_of_words = sentence.split()
    for wordindex in range(0, len(list_of_words)):
        if len(str(list_of_words[wordindex])) > 4:
            list_of_words[wordindex] = ''.join(
                reversed(str(list_of_words[wordindex])))
        alteredscentence = ' '.join(list_of_words)
    print(alteredscentence)
    return None


spin_words("This sentence is a sentence")
