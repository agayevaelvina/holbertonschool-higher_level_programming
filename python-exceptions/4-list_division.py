#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        value = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
                print("wrong type")
            else:
                try:
                    value = a / b
                except ZeroDivisionError:
                    print("division by 0")
                    value = 0
        except IndexError:
            print("out of range")
        finally:
