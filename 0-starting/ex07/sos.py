# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/27 22:12:01 by jihoolee          #+#    #+#              #
#    Updated: 2024/08/11 01:04:47 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def morse(text: str) -> str:
    """Converts the input text to morse code.

    Args:
    - text (str): The input text.

    Returns:
    - str: The morse code of the input text.

    Raises:
        AssertionError: If the input text contains characters other than
        alphabets and spaces.
    """
    NESTED_MORSE: dict[str, str] = {
        ' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
        'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..'
    }
    try:
        result: str = ' '.join([NESTED_MORSE[char.upper()] for char in text])
    except KeyError:
        raise AssertionError('the arguments are bad')
    return result


def main(argv: list[str]) -> None:
    assert len(argv) == 2, 'the arguments are bad'
    print(morse(argv[1]))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(f'AssertionError: {e}')
        sys.exit(1)
