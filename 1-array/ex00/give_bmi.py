# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    give_bmi.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/17 23:24:43 by jihoolee          #+#    #+#              #
#    Updated: 2024/08/18 21:57:17 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the BMI (Body Mass Index) for a list of heights and weights.

    Args:
        height (list[int | float]): A list of heights.
        weight (list[int | float]): A list of weights.

    Returns:
        list[int | float]: A list of calculated BMI values.

    Raises:
        ValueError:
            If the length of height and weight lists are not the same.
        ValueError:
            If any height or weight value is not positive.
        ValueError:
            If any height or weight value is not of type int or float.
    """
    try:
        if len(height) != len(weight):
            raise ValueError(
                "The length of height and weight should be the same."
            )
        bmi: list[int | float] = []

        for height, weight in zip(height, weight):
            if (not isinstance(height, (int, float))
                    or not isinstance(weight, (int, float))):
                raise ValueError(
                    "Height and weight should be int or float.")
            if height <= 0 or weight <= 0:
                raise ValueError(
                    "Height and weight should be positive.")

            bmi.append(weight / (height ** 2))
        return bmi
    except Exception as error:
        print(f"Error: {error}")
        return []


def apply_limit(bmi: list[int | float], limits: int) -> list[bool]:
    """
    Apply a limit to each BMI value in the given list and return a list of
    booleans indicating whether each BMI value is below the limit.

    Args:
        bmi (list[int | float]): A list of BMI values.
        limits (int): The limit to be applied to each BMI value.

    Returns:
        list[bool]: A list of booleans indicating whether each BMI value is
        above the limit.

    Raises:
        ValueError:
            If any BMI value is not of type int or float.
    """
    try:
        if not isinstance(limits, int):
            raise ValueError("Limit should be int value only.")
        result: list[bool] = []

        for value in bmi:
            if not isinstance(value, (int, float)):
                raise ValueError("BMI should be int or float value.")
            result.append(value > limits)
        return result
    except Exception as error:
        print(f"Error: {error}")
        return []
