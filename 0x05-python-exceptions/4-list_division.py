#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divides element in list 1 by element in list 2

    args:
        my_list_1: first list
        my_list_2: second list
        list_length: list length - can be bigger than the 2 list

    Return: a new list containing dividends
    """

    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
            result = 1
        except IndexError:
            new_list.append(0)
            result = -1
        except (TypeError, ValueError):
            new_list.append(0)
            result = 0
        except ZeroDivisionError:
            new_list.append(0)
            result = None
        finally:
            if result == 0:
                print("wrong type")
            if result is None:
                print("division by 0")
            if result == -1:
                print("out of range")
    return new_list
