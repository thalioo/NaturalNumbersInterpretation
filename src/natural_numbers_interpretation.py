import argparse
from phone_number import PhoneNumber
import re


def get_input_from_prompt():
    phone_number = input('Please provide valid phone number.\n'
                         'Sequences of numbers must be seperated'
                         'by space and each sequence must be '
                         'up to 3 digits:\n')
    return phone_number


def read_from_file(file):
    try:
        phone_numbers_list = []
        with open(file) as f:
            phone_numbers_list = f.read().splitlines()
        return phone_numbers_list
    except FileNotFoundError:
        print("The file does not exist")
        return


def validate_input(phone_number):
    for token in phone_number:
        if len(token) > 3 or not token.isdigit():
            print("Invalid Input.")
            return
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numbers",
                        help="""Input phone numbers as
                        string. If multiple seperated by space""", nargs='*')
    parser.add_argument("-f", "--file", help="Input file of numbers.")
    parser.add_argument("-m", "--method", choices=["a", "b"],
                        help="b for Basic a for Advanced. Default is basic.", default="a")
    args = parser.parse_args()
    if args.numbers:
        phone_numbers = args.numbers
    elif args.file:
        phone_numbers = read_from_file(args.file)
    else:
        phone_numbers = [get_input_from_prompt()]

    if args.method == 'b':
        print("Running Basic Level")
        for phone_num in phone_numbers:
            print(phone_num)
            if validate_input(phone_num.split(" ")):
                phone_num_obj = PhoneNumber(phone_num)
                num, valid = phone_num_obj.basic()
                print(num, "phone number : ", valid)
            print('-------------')
    else:
        print("Running Advanced Level")
        for phone_num in phone_numbers:
            print(phone_num)
            if validate_input(phone_num.split(" ")):
                phone_num_obj = PhoneNumber(phone_num)
                interpretations = sorted(phone_num_obj.advanced(), reverse=True)
                for idx, item in enumerate(interpretations):
                    print("Interpretation ", idx+1, ": ",
                          item[0], "phone number : ", item[1])
                print('-------------')
