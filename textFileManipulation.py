"""
Whiting in a .txt file, reading a .txt file.
Calculating the sum of a .txt file
"""
__author__ = 'Gareth'


def main():
    enter_name()
    read_name()
    read_numbers()


def enter_name():
    name = input("What is your name? ")
    list = open('name.txt', mode='w')
    list.write(name)


def read_name():
    names = open('name.txt', mode='r')
    name = names.readline()
    print("Your name is {}".format(name))


def read_numbers():
    numbers = 0
    txt_numbers = open('numbers.txt', mode='r')
    for line in txt_numbers:
        numbers += int(line)
    print("The sum of the numbers is: {}".format(numbers))


if __name__ == "__main__":
    main()