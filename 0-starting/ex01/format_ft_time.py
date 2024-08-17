# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/13 17:27:14 by jihoolee          #+#    #+#              #
#    Updated: 2024/07/13 17:27:14 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time


def main() -> None:
    curr_time: float = time.time()
    print(f'Seconds since January 1, 1970: {curr_time:,.4f} or '
          f'{curr_time:.2e} in scientific notation')
    print(time.strftime('%b %d %Y', time.localtime(curr_time)))


if (__name__ == '__main__'):
    main()
