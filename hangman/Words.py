from random import randint

WORDLIST = 'wordlist.txt'


def get_random_word(min_word_length: int):
    """Get a random word from the wordlist"""
    num_words_processed = 0
    current_word = None
    with open(WORDLIST, 'r') as f:
        for word in f:
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            num_words_processed += 1
            if randint(1, num_words_processed) == 1:
                current_word = word

    return current_word


if __name__ == '__main__':
    print(get_random_word(3))
    print(get_random_word(6))