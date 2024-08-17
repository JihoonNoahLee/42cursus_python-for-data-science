# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/14 00:32:28 by jihoolee          #+#    #+#              #
#    Updated: 2024/07/14 20:35:42 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_filter(function, iterable):
    """Filters the elements of an iterable based on a given function.

    Args:
        function: A function that takes an item from the iterable as input and
            returns a boolean value. Can be None
        iterable: An iterable object containing the elements to be filtered.

    Returns:
        A generator object that yields the elements from the iterable that
            satisfy the given function.
    """
    if function:
        return (item for item in iterable if function(item))
    else:
        return (item for item in iterable if item)
