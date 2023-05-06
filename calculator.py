class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    
    def kilos_to_stone(self, kilos):
        return kilos * 0.157473
    
    def gigabytes_to_bytes(self, gigabytes):
        return gigabytes * 1000000000
    
    def inches_to_centimeters(self, inches):
        return inches * 2.54
    
    def days_to_seconds(self, days):
        return days * 86400
    
    def decimal_to_binary(self, decimal):
        return bin(decimal)
    
    def decimal_to_octal(self, decimal):
        return oct(decimal)
    
    def decimal_to_hexadecimal(self, decimal):
        return hex(decimal)
    
    def calculate(self, equation):
        try:
            result = eval(equation)
            self.history.append(f"{equation} = {result}")
            return result
        except:
            return "Invalid equation"
    
    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history = []

# console-based interface
calculator = Calculator()

while True:
    print("                                                                                                                                                                   ")
    print("A python based calculator                                                                                                                                           ")
    print("                                                                                                                                                                   ")
    print("    ,o888888o.           .8.          8 8888         ,o888888o.    8 8888      88 8 8888                  .8.    8888888 8888888888 ,o888888o.     8 888888888o.   ")
    print("   8888     `88.        .888.         8 8888        8888     `88.  8 8888      88 8 8888                 .888.         8 8888    . 8888     `88.   8 8888    `88.  ")
    print(",8 8888       `8.      :88888.        8 8888     ,8 8888       `8. 8 8888      88 8 8888                :88888.        8 8888   ,8 8888       `8b  8 8888     `88  ")
    print("88 8888               . `88888.       8 8888     88 8888           8 8888      88 8 8888               . `88888.       8 8888   88 8888        `8b 8 8888     ,88  ")
    print("88 8888              .8. `88888.      8 8888     88 8888           8 8888      88 8 8888              .8. `88888.      8 8888   88 8888         88 8 8888.   ,88'  ")
    print("88 8888             .8`8. `88888.     8 8888     88 8888           8 8888      88 8 8888             .8`8. `88888.     8 8888   88 8888         88 8 888888888P'   ")
    print("88 8888            .8' `8. `88888.    8 8888     88 8888           8 8888      88 8 8888            .8' `8. `88888.    8 8888   88 8888        ,8P 8 8888`8b       ")
    print("`8 8888       .8' .8'   `8. `88888.   8 8888     `8 8888       .8' ` 8888     ,8P 8 8888           .8'   `8. `88888.   8 8888   `8 8888       ,8P  8 8888 `8b.     ")
    print("   8888     ,88' .888888888. `88888.  8 8888        8888     ,88'    8888   ,d8P  8 8888          .888888888. `88888.  8 8888    ` 8888     ,88'   8 8888   `8b.   ")
    print("    `8888888P'  .8'       `8. `88888. 8 888888888888 `8888888P'       `Y88888P'   8 888888888888 .8'       `8. `88888. 8 8888       `8888888P'     8 8888     `88. ")
    print("                                                                                                                                                                   ")
    print("                                                                                                                                                         By Charlie")
    print("                                                                                                                                                                   ")
    print("Calculator Commands:")
    print("--------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Kilos to Stone")
    print("6. Gigabytes to bytes")
    print("7. Inches to Centimeters")
    print("8. Days to Seconds")
    print("9. Decimal to Binary")
    print("10. Decimal to Octal")
    print("11. Decimal to Hexadecimal")
    print("12. Advanced Arithmetic")
    print("13. History")
    print("14. Clear History")
    print("15. Quit")

    choice = input("Enter your choice (1-15): ")

    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculator.add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculator.subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculator.multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculator.divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    elif choice == "5":
        kilos = float(input("Enter weight in Kilos: "))
        result = calculator.kilos_to_stone(kilos)
        print(f"{kilos} Kilos = {result} Stones")
    elif choice == "6":
        gigabytes = float(input("Enter size in Gigabytes: "))
        result = calculator.gigabytes_to_bytes(gigabytes)
        print(f"{gigabytes} Gigabytes = {result} Bytes")
    elif choice == "7":
        inches = float(input("Enter length in Inches: "))
        result = calculator.inches_to_centimeters(inches)
        print(f"{inches} Inches = {result} Centimeters")
    elif choice == "8":
        days = float(input("Enter time in Days: "))
        result = calculator.days_to_seconds(days)
        print(f"{days} Days = {result} Seconds")
    elif choice == "9":
        decimal = int(input("Enter a decimal number: "))
        result = calculator.decimal_to_binary(decimal)
        print(f"{decimal} Decimal = {result} Binary")
    elif choice == "10":
        decimal = int(input("Enter a decimal number: "))
        result = calculator.decimal_to_octal(decimal)
        print(f"{decimal} Decimal = {result} Octal")
    elif choice == "11":
        decimal = int(input("Enter a decimal number: "))
        result = calculator.decimal_to_hexadecimal(decimal)
        print(f"{decimal} Decimal = {result} Hexadecimal")
    elif choice == "12":
        equation = input("Enter an equation: ")
        result = calculator.calculate(equation)
        print(result)
    elif choice == "13":
        history = calculator.get_history()
        for entry in history:
            print(entry)
    elif choice == "14":
        calculator.clear_history()
        print("History cleared")
    elif choice == "15":
        break
    else:
        print("Invalid choice")
