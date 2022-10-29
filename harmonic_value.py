def harmonic_vale(num_, _num2):
    """
    Printing The Harmonic Value
    """
    result = 0
    for i in range(num_, _num2):
        _result = (1/i)
        result = (result + (1 / i))
        print("ranges from:{} to {} harmonic values:{}".format(num_, num2, _result))
    print("the entire value:{}".format(result))


if __name__ == '__main__':
    num1 = int(input("enter the number"))
    num2 = int(input("enter the number"))
    harmonic_vale(num1, num2)
