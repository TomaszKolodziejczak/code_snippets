"""
Longest Word

Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string.
If there are two or more words that are the same length, return the first word from the string with that length.
Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
Examples

Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
"""
import string


def longest_word(sen):
    words_list = sen.translate(str.maketrans('', '', string.punctuation)).split()
    longest = max(words_list, key=len)
    return longest


if __name__ == "__main__":
  print(longest_word("Let's start with professional experience :)"))