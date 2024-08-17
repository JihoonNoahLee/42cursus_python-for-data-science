# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterstring.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/14 00:35:14 by jihoolee          #+#    #+#              #
#    Updated: 2024/07/27 22:11:11 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def filter_words_by_length(words: list[str], length: int) -> list[str]:
    """Filters the words in the list of words by length.

    Args:
        text (list[str]): The input words.
        length (int): The minimum length of words to be included in the result.

    Returns:
        list[str]: A list of words in the text that have a length greater than
            the given length.
    """
    return list(filter(lambda x: len(x) > length, words))


def main(argv: list[str]) -> None:
    assert len(argv) == 3, 'the arguments are bad'
    assert argv[1].isprintable(), 'the arguments are bad'

    try:
        word_len: int = int(argv[2])
    except ValueError:
        raise AssertionError('the arguments are bad')
    print(filter_words_by_length(argv[1].split(), word_len))


if __name__ == '__main__':
    try:
        main(sys.argv)
    except AssertionError as e:
        print(f'AssertionError: {e}')
        sys.exit(1)
