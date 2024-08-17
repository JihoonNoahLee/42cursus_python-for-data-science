# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/13 17:27:27 by jihoolee          #+#    #+#              #
#    Updated: 2024/07/13 17:28:27 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def isnan(num: float) -> bool:
    if (num != num):
        return True
    return False


def NULL_not_found(object: any) -> int:
    if object is None:
        print(f'Nothing: {object} {type(object)}')
    elif isinstance(object, float) and isnan(object):
        print(f'Cheese: {object} {type(object)}')
    elif isinstance(object, int) and object == 0:
        print(f'Zero: {object} {type(object)}')
    elif object == '':
        print(f'Empty: {object} {type(object)}')
    elif object is False:
        print(f'Fake: {object} {type(object)}')
    else:
        print('Type not Found')
        return 1
    return 0
