#!/usr/bin/env python3
# Created by Marc Coffi
# Created in April 2022
# This is a programs that finds month base on the number inputted


user_input = input("Enter a number representing a month: ")
# Cast user input to a integer
user_num = int(user_input)
# Check the numbers and display the output
def find_month(month):
    months = {
        1: "{} is January.".format(month),
        2: "{} is February.".format(month),
        3: "{} is March.".format(month),
        4: "{} is April.".format(month),
        5: "{} is May.".format(month),
        6: "{} is June.".format(month),
        7: "{} is July.".format(month),
        8: "{} is August.".format(month),
        9: "{} is September.".format(month),
        10: "{} is October.".format(month),
        11: "{} is November.".format(month),
        12: "{} is December.".format(month),
    }
    return months.get(month, "Error. {} does not represent a month.".format(month))


if __name__ == "__main__":
    print(find_month(user_num))
