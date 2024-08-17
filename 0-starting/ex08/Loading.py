# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/10 20:41:12 by jihoolee          #+#    #+#              #
#    Updated: 2024/08/11 01:06:19 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_tqdm(lst: range) -> None:
    """
    Prints the progress of an iteration using a progress bar.

    Args:
        lst (range): The range of values to iterate over.

    Yields:
        int: The current value of the iteration.

    Raises:
        nothing.
    """

    def print_progress(cur_it: int, total_it: int) -> None:
        """
        Prints the progress of a task as a percentage and a progress bar.

        Args:
        - cur_it (int): The current iteration.
        - total_it (int): The total number of iterations.

        Returns:
        None

        Example:
        >>> print_progress(3, 10)
        30%|[====>                                               ]| 3/10
        """

        progress_percent: int = int(cur_it / total_it * 100)
        progress_bar: str = '=' * ((progress_percent - 1) // 2) + '>'
        status: str = (
            f'\r{progress_percent:>3}%|[{progress_bar:<50}]| '
            f'{cur_it}/{total_it}'
        )
        print(status, end='')

    cur_it: int = 0

    for it in lst:
        cur_it += 1
        print_progress(cur_it, len(lst))
        yield it
    print()
