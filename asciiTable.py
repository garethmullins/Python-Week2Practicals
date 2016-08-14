def main():
    input_codes = input("Enter the ASCII codes, seperate the codes with commas \",\" ")
    code = input_codes.split(",")
    for i in range(0, len(code)):
        print("{:<5} {}".format(code[i], chr(int(code[i]))))


if __name__ == "__main__":
        main()




def main():
    LOWER = 0
    UPPER = 10
    codes = get_number(LOWER, UPPER)
    for i in range(0, len(codes)):
        print("{:<5} {}".format(codes[i], chr(int(codes[i]))))

def get_number(LOWER, UPPER):
    input_codes = input("Enter the ASCII codes between {} and {}, seperate the codes with commas \",\" ". format(LOWER, UPPER))
    codes = input_codes.split(",")
    errors = 1
    while errors > 0:
        errors = 0
        for i in range(0, len(codes)):
            if int(codes[i]) < LOWER or int(codes[i]) > UPPER:
                errors += 1
        if errors > 0:
            print("An invalid code was entered.")
            input_codes = input("Enter the ASCII codes between {} and {}, seperate the codes with commas \",\" ". format(LOWER, UPPER))
            codes = input_codes.split(",")
    return codes



if __name__ == "__main__":
        main()