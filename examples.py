import random

name = "Gibson L - 5 CES"
year = 1922
cost = 16035.40
# The ‘old’ manual way to format text:
print("My guitar: " + name + ", first made in " + str(year))

print()
print()

# A better way using str.format():
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))


print()
print()

# Formatting currency:
print("My {} would cost ${:,.2f}".format(name, cost))

print()
print()

# Aligning columns:
numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
    print("Number {0} is {1:>5}".format(i + 1, numbers[i]))

print()
print()

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

print()
print()
print()
print()
print()

print("Tab 1" + '\t' + "Tab 2" + '\t' + "Tab 3")

print()
print()
print()
print()
print()

print("Line 1" + '\n' + "Line 2" + '\n' + "Line 3")

print()
print()
print()
print()

string = "1, first number"

x = string.split(",")

print(x[0])
print(x[1])

print()
print()
print()
print()

s = "madam I'm adam"
reversed = s[::-1]
print(reversed)

print()
print()
print()

word = "1hello"
print(word.find("l"))

print()
print()
print()

file_name = input("Text file name: ")
if not file_name.endswith(".txt"):
    print("Let me stop you right there")

print()
print()
print()

file_name = input("Phone number: ")
if not file_name.startswith("07"):
    print("Let me stop you right there")

print()
print()
print()

print("{:>10s} is {:<10d} years old.".format('Bill', 25))

print()
print()
print()

name = "Monty"
money = 73.6
print("{} has ${:.2f}".format(name, money))
