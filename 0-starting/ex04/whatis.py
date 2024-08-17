# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/13 22:16:32 by jihoolee          #+#    #+#              #
#    Updated: 2024/07/13 22:19:19 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def is_odd(num: int) -> bool:
    if num % 2:
        return True
    return False


def main(argv: list[str]) -> None:
    if len(argv) == 1:
        return
    assert len(argv) <= 2, 'more than one argument is provided'
    try:
        num: int = int(argv[1])
    except ValueError:
        raise AssertionError('argument is not an integer')
    print(f"I'm {'Odd' if is_odd(num) else 'Even'}.")


if __name__ == '__main__':
    main(sys.argv)
