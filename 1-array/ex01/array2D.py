# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    array2D.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/18 22:01:13 by jihoolee          #+#    #+#              #
#    Updated: 2024/08/18 22:33:12 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    print(f'My shape is: ({len(family)}, {len(family[0])})')
    return family[start:end]
