def main():
    input_codes = input("Enter the ASCII codes, seperate the codes with commas \",\" ")
    code = input_codes.split(",")
    for i in range(0, len(code)):
        print("{:<5} {}".format(code[i], chr(int(code[i]))))


if __name__ == "__main__":
        main()