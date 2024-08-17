# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/13 23:01:20 by jihoolee          #+#    #+#              #
#    Updated: 2024/07/14 00:33:36 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def count_characters(text: str) -> tuple[int]:
    """Counts the number of characters in the given text.

    Args:
        text (str): The input text.

    Returns:
        tuple[int]: A tuple containing the counts of the following characters:
            - Number of uppercase letters
            - Number of lowercase letters
            - Number of punctuation characters
            - Number of whitespace characters
            - Number of digits
    """
    PUNCTUTATION: str = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    upper_case_cnt: int = len([c for c in text if c.isupper()])
    lower_case_cnt: int = len([c for c in text if c.islower()])
    punctuation_cnt: int = len([c for c in text if c in PUNCTUTATION])
    space_cnt: int = len([c for c in text if c.isspace()])
    digit_cnt: int = len([c for c in text if c.isdigit()])
    return (upper_case_cnt, lower_case_cnt, punctuation_cnt,
            space_cnt, digit_cnt)


def main(argv: list[str]) -> None:
    """Main function to count the number of characters in a given text.

    Args:
        argv (list[str]): List of command-line arguments.

    Returns:
        None
    """
    assert len(argv) <= 2, 'more than one argument is provided'

    if len(argv) == 1:
        print('What is the text to count?')
        text: str = sys.stdin.readline()
    else:
        text: str = argv[1]

    (upper_case_cnt, lower_case_cnt, punctuation_cnt,
     space_cnt, digit_cnt) = count_characters(text)
    print(f"The text contains {len(text)} characters:")
    print(f"{upper_case_cnt} upper letters")
    print(f"{lower_case_cnt} lower letters")
    print(f"{punctuation_cnt} punctuation marks")
    print(f"{space_cnt} spaces")
    print(f"{digit_cnt} digits")


if __name__ == '__main__':
    try:
        main(sys.argv)
    except AssertionError as ae:
        print(f'AssertionError: {ae}')
