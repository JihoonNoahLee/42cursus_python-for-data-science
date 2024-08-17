# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/13 17:27:09 by jihoolee          #+#    #+#              #
#    Updated: 2024/07/13 17:27:09 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = 'World'
ft_tuple = ('Hello', 'Korea!')
ft_set.remove('tutu!')
ft_set.add('Seoul!')
ft_dict['Hello'] = '42Seoul!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
