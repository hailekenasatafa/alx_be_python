# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR\s*=\s*9\/5 

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(Fahrenheit):
    """ Converts Fahrenheit to Celsius."""
    return (Fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """ Converts Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program to interact with the user
def main():
    while True:
        try:
            # User input for temperature
            temperature = float(input("Enter the temperature to convert: "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

    # User input for unit
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            break  # Exit loop if input is valid
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    # Conversion and output
    if unit == 'C':
        Fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")
    else:  # unit == 'F'
        Celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")

# Entry point of the script
if __name__ == "__main__":
    main()
