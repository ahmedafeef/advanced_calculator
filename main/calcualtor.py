import math

def calculator():
    print("Welcome to the advanced calculator!"      )
    print("Please select an operation:"             )
    print("1. Addition"                          )
    print("2. Subtraction"                         )
    print("3. Multiplication"                      )
    print("4. Division"                         )
    print("5. Exponentiation"                     )
    print("6. Square root"                      )
    print("7. Logarithm"                              )
    print("8. Trigonometric functions"                    )
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", num1 + num2)

    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", num1 - num2)

    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", num1 * num2)

    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", num1 / num2)

    elif choice == 5:
        num1 = float(input("Enter base: "))
        num2 = float(input("Enter exponent: "))
        print("Result: ", num1 ** num2)

    elif choice == 6:
        num = float(input("Enter number: "))
        print("Result: ", math.sqrt(num))

    elif choice == 7:
        num = float(input("Enter number: "))
        base = float(input("Enter base: "))
        print("Result: ", math.log(num, base))

    elif choice == 8:
        num = float(input("Enter angle in degrees: "))
        print("sin({}) = {}".format(num, math.sin(math.radians(num))))
        print("cos({}) = {}".format(num, math.cos(math.radians(num))))
        print("tan({}) = {}".format(num, math.tan(math.radians(num))))
        print("cosec({}) = {}".format(num, 1 / math.sin(math.radians(num))))
        print("sec({}) = {}".format(num, 1 / math.cos(math.radians(num))))
        print("cot({}) = {}".format(num, 1 / math.tan(math.radians(num))))

    elif choice == 9:
        print("Exiting...")
        return

    else:
        print("Invalid choice. Please try again.")

    calculator()

calculator()