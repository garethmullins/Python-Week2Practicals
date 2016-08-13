def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            denominator = int(input("The number \"0\" was entered as the denominator, please renter the denominator."))
        fraction = numerator / denominator
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    print("Finished.")


if __name__ == "__main__":
    main()