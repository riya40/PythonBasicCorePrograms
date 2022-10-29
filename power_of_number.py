def power_of_value(num_):
    """
    Calculating Power Of 2
    Printing the table from user input
    """
    for x in range(1, num_):
        print(2 ** x)


if __name__ == '__main__':
    num = int(input("enter the number"))
    power_of_value(num)
