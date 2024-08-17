# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/11 01:10:14 by jihoolee          #+#    #+#              #
#    Updated: 2024/08/17 22:26:13 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    url='https://github.com/JihoonNoahLee/42cursus_python-for-data-science/tree/main/0-starting/ex09',  # noqa
    author='jihoolee',
    author_email='jihoolee@student.42seoul.kr',
    license='MIT',
    packages=find_packages(),
    install_requires=[]
)
