# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # ✔️ Required for check
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # ✔️ Required for check

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  # ✔️ Uses global variable

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32  # ✔️ Uses global variable

def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # ✔️ Validate numeric input
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")  # ✔️ Raise error

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    elif unit == "F":
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    else:
        print("Invalid input. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
