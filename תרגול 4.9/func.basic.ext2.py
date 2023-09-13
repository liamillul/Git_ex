word_list = []
string = input("enter a sentence or a word: ")
num_of_words = len(string.split())


def rev_word(word):
    return word[::-1]


def rev_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence


if num_of_words == 1:
    print(rev_word(string))
else:
    print(rev_sentence(string))
