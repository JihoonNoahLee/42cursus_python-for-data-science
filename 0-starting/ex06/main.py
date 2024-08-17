# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/14 00:57:19 by jihoolee          #+#    #+#              #
#    Updated: 2024/07/27 18:50:20 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ft_filter import ft_filter


def test_ft_filter():
    # Test case 1: Filter even numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_numbers = ft_filter(lambda x: x % 2 == 0, numbers)
    expected_output = filter(lambda x: x % 2 == 0, numbers)
    assert list(filtered_numbers) == list(expected_output), \
        f'Test case 1 failed. Expected: {expected_output}, '\
        f'Got: {filtered_numbers}'

    # Test case 2: Filter strings with length greater than 5
    strings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    filtered_strings = ft_filter(lambda x: len(x) > 5, strings)
    expected_output = filter(lambda x: len(x) > 5, strings)
    assert list(filtered_strings) == list(expected_output), \
        f'Test case 2 failed. Expected: {expected_output}, '\
        f'Got: {filtered_strings}'

    # Test case 3: Filter positive numbers
    numbers = [-3, -2, -1, 0, 1, 2, 3]
    filtered_numbers = ft_filter(lambda x: x > 0, numbers)
    expected_output = filter(lambda x: x > 0, numbers)
    assert list(filtered_numbers) == list(expected_output), \
        f'Test case 3 failed. Expected: {expected_output}, '\
        f'Got: {filtered_numbers}'

    print('All test cases passed!')


def main() -> None:
    test_ft_filter()


if __name__ == '__main__':
    main()
