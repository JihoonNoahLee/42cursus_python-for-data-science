# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tester.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/10 20:13:13 by jihoolee          #+#    #+#              #
#    Updated: 2024/08/10 20:18:38 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
    sleep(0.005)

print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()
