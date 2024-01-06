#!/usr/bin/python3
def divisible_by_2(my_list=[]):
  divisibility_list = []
  for element in my_list:
    divisibility_list.append(element % 2 == 0)
    return divisibility_list
