#!/usr/bin/python3
def max_integer(my_list=[]):
  if not my_list:
    return None

  biggest = my_list[0]

  for element in my_list[1:]:
    if element > biggest:
      biggest = element

  return biggest
