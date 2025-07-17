 def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def temperature_converter():
    print("Temperature Converter")
    print("Choose the input scale:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        temp = float(input("Enter temperature in Celsius: "))
        print(f"Fahrenheit: {celsius_to_fahrenheit(temp):.2f}")
        print(f"Kelvin: {celsius_to_kelvin(temp):.2f}")
    elif choice == 2:
        temp = float(input("Enter temperature in Fahrenheit: "))
        print(f"Celsius: {fahrenheit_to_celsius(temp):.2f}")
        print(f"Kelvin: {fahrenheit_to_kelvin(temp):.2f}")
    elif choice == 3:
        temp = float(input("Enter temperature in Kelvin: "))
        print(f"Celsius: {kelvin_to_celsius(temp):.2f}")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(temp):.2f}")
    else:
        print("Invalid choice!")

# Run the program
temperature_converter()