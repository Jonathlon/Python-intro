first_number = int(input("Input a number: "))
second_number = int(input("Input another number: "))
operater = input("add or subtract: ")

if operater == "+":
    print(first_number + second_number)

elif operater == "-":
    print(first_number - second_number)

else:
    print("Only add or subtract")