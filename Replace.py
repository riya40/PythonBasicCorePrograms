"""
Taking The Input String From User
Replace The Template By Using The User_input
"""

def replace_name(input_string , user_input , replace_input):

    print(input_string.replace(user_input,replace_input,))


if __name__ == '__main__':
    input_string = input("enter the input:")
    user_input = input("enter which need to be replace:")
    replace_input = input("enter input for replace:")
    replace_name(input_string,user_input,replace_input)

