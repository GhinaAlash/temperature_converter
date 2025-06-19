temperature_converter.py

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Choose conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    c = float(input("Enter temperature in Celsius: "))
    f = celsius_to_fahrenheit(c)
    print("Temperature in Fahrenheit:", round(f, 2))
elif choice == '2':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = fahrenheit_to_celsius(f)
    print("Temperature in Celsius:", round(c, 2))
else:
    print("Invalid choice.")


---

🔹 File: README.md

# Temperature Converter 🌡️

This is a simple Python program that converts temperature between Celsius and Fahrenheit.

## Features
- Convert Celsius to Fahrenheit
- Convert Fahrenheit to Celsius

## Language
Python 3

## Files
- temperature_converter.py: Main script
