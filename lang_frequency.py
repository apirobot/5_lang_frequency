import re
import argparse
from collections import Counter

parser = argparse.ArgumentParser(description='Frequency Analysis of Words')
parser.add_argument('path', metavar='DIR', help='path to the text file')
parser.add_argument('--num', type=int, default=10,
                    help='number of most common words to display')
args = parser.parse_args()


def load_data(filepath):
    with open(filepath) as file_handler:
        return file_handler.read()


def get_most_frequent_words_and_their_frequency(text, num=10):
    """Gets ``num`` most common words and their frequency.

    :returns: List of tuples. Tuple contains word and frequency.
    :Example:
        [('the', 164), ('and', 161), ('a', 138), ('python', 138),
        ('of', 131), ('is', 102), ('to', 91), ('in', 88), ('on', 56)]
    """
    word_list = re.sub(pattern='[^\w]', repl=' ', string=text).split()
    counter = Counter(word_list)
    return counter.most_common(num)


def main():
    text = load_data(args.path)
    words_and_freq = get_most_frequent_words_and_their_frequency(text, args.num)

    print('Most common words:')
    print('\n'.join('%s: %d' % (t[0], t[1]) for t in words_and_freq))


if __name__ == '__main__':
    main()
