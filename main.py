from converters import (
    pound_to_kg, kg_to_pound,
    inch_to_meter, meter_to_inch,
    fahrenheit_to_celsius, celsius_to_fahrenheit,
    gallon_to_liter, liter_to_gallon
)

def main():
    while True:
        print("\n===== Imperial ↔ Metric Converter =====")
        print("1. Convert weight (lb ↔ kg)")
        print("2. Convert height (inch ↔ meter)")
        print("3. Convert temperature (°F ↔ °C)")
        print("4. Convert volume (gallon ↔ liter)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                weight = float(input("Enter the weight: "))
                unit_from = input("From lb or kg? ").lower()
                if unit_from == "lb":
                    print(f"{weight} lb = {pound_to_kg(weight):.2f} kg")
                elif unit_from == "kg":
                    print(f"{weight} kg = {kg_to_pound(weight):.2f} lb")
                else:
                    print("Unknown unit.")

            elif choice == "2":
                height = float(input("Enter the height: "))
                unit_from = input("From inch or m? ").lower()
                if unit_from == "inch":
                    print(f"{height} inches = {inch_to_meter(height):.2f} meters")
                elif unit_from == "m":
                    print(f"{height} meters = {meter_to_inch(height):.2f} inches")
                else:
                    print("Unknown unit.")

            elif choice == "3":
                temp = float(input("Enter the temperature: "))
                unit_from = input("From f or c? ").lower()
                if unit_from == "f":
                    print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
                elif unit_from == "c":
                    print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
                else:
                    print("Unknown unit.")

            elif choice == "4":
                volume = float(input("Enter the volume: "))
                unit_from = input("From g (gallon) or l (liter)? ").lower()
                if unit_from == "g":
                    print(f"{volume} gallons = {gallon_to_liter(volume):.2f} liters")
                elif unit_from == "l":
                    print(f"{volume} liters = {liter_to_gallon(volume):.2f} gallons")
                else:
                    print("Unknown unit.")

            elif choice == "5":
                print("Goodbye! 👋")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
