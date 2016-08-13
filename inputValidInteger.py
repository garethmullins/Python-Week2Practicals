"""
CP1404/CP5632 - Practical
"""


def main():
    finished = False
    result = 0
    while not finished:
        try:
            result = int(input("Please enter an integer. "))
            finished = True
            pass
        except:
            print("\n"+"Please enter a valid integer.")
    print("Valid result is:", result)


if __name__ == "__main__":
        main()