def leap_year(_year):
    """
    Determining the given Year is Leap Or Not
    """
    if (_year % 400 == 0) or (_year % 100 != 0) and (_year % 4 == 0):
        print(_year, "leap year")
    else:
        print(_year, "not leap year")


if __name__ == '__main__':
    year = int(input("enter the year"))
    leap_year(year)
