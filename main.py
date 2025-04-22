import tkinter as tk
from tkinter import ttk, messagebox
from converters import (
    pound_to_kg, kg_to_pound,
    inch_to_meter, meter_to_inch,
    fahrenheit_to_celsius, celsius_to_fahrenheit,
    gallon_to_liter, liter_to_gallon
)


class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Imperial ↔ Metric Converter")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Style configuration
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'))

        self.create_widgets()

    def create_widgets(self):
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=10)

        ttk.Label(
            header_frame,
            text="Imperial ↔ Metric Converter",
            style='Header.TLabel'
        ).pack()

        # Conversion type selection
        type_frame = ttk.Frame(self.root)
        type_frame.pack(pady=10)

        ttk.Label(type_frame, text="Select conversion type:").pack()

        self.conversion_type = tk.StringVar()
        conversions = [
            ("Weight (lb ↔ kg)", "weight"),
            ("Height (inch ↔ m)", "height"),
            ("Temperature (°F ↔ °C)", "temp"),
            ("Volume (gallon ↔ liter)", "volume")
        ]

        for text, mode in conversions:
            ttk.Radiobutton(
                type_frame,
                text=text,
                variable=self.conversion_type,
                value=mode,
                command=self.update_conversion_fields
            ).pack(anchor='w', padx=20)

        # Conversion fields
        self.fields_frame = ttk.Frame(self.root)
        self.fields_frame.pack(pady=10)

        # Initially empty, will be populated by update_conversion_fields
        self.input_entry = None
        self.from_var = None
        self.to_var = None

        # Result display
        self.result_label = ttk.Label(self.root, text="", font=('Arial', 12))
        self.result_label.pack(pady=10)

        # Convert button
        ttk.Button(
            self.root,
            text="Convert",
            command=self.perform_conversion
        ).pack(pady=10)

    def update_conversion_fields(self):
        # Clear previous fields
        for widget in self.fields_frame.winfo_children():
            widget.destroy()

        # Create new fields based on selection
        conversion_type = self.conversion_type.get()

        ttk.Label(self.fields_frame, text="Value to convert:").grid(row=0, column=0, padx=5, pady=5)
        self.input_entry = ttk.Entry(self.fields_frame, width=15)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)

        self.from_var = tk.StringVar()
        self.to_var = tk.StringVar()

        if conversion_type == "weight":
            ttk.Label(self.fields_frame, text="From:").grid(row=1, column=0, padx=5, pady=5)
            ttk.Combobox(
                self.fields_frame,
                textvariable=self.from_var,
                values=["Pounds (lb)", "Kilograms (kg)"],
                state="readonly",
                width=15
            ).grid(row=1, column=1, padx=5, pady=5)

            ttk.Label(self.fields_frame, text="To:").grid(row=2, column=0, padx=5, pady=5)
            ttk.Combobox(
                self.fields_frame,
                textvariable=self.to_var,
                values=["Kilograms (kg)", "Pounds (lb)"],
                state="readonly",
                width=15
            ).grid(row=2, column=1, padx=5, pady=5)

        elif conversion_type == "height":
            ttk.Label(self.fields_frame, text="From:").grid(row=1, column=0, padx=5, pady=5)
            ttk.Combobox(
                self.fields_frame,
                textvariable=self.from_var,
                values=["Inches (in)", "Meters (m)"],
                state="readonly",
                width=15
            ).grid(row=1, column=1, padx=5, pady=5)

            ttk.Label(self.fields_frame, text="To:").grid(row=2, column=0, padx=5, pady=5)
            ttk.Combobox(
                self.fields_frame,
                textvariable=self.to_var,
                values=["Meters (m)", "Inches (in)"],
                state="readonly",
                width=15
            ).grid(row=2, column=1, padx=5, pady=5)

        elif conversion_type == "temp":
            ttk.Label(self.fields_frame, text="From:").grid(row=1, column=0, padx=5, pady=5)
            ttk.Combobox(
                self.fields_frame,
                textvariable=self.from_var,
                values=["Fahrenheit (°F)", "Celsius (°C)"],
                state="readonly",
                width=15
            ).grid(row=1, column=1, padx=5, pady=5)

            ttk.Label(self.fields_frame, text="To:").grid(row=2, column=0, padx=5, pady=5)
            ttk.Combobox(
                self.fields_frame,
                textvariable=self.to_var,
                values=["Celsius (°C)", "Fahrenheit (°F)"],
                state="readonly",
                width=15
            ).grid(row=2, column=1, padx=5, pady=5)

        elif conversion_type == "volume":
            ttk.Label(self.fields_frame, text="From:").grid(row=1, column=0, padx=5, pady=5)
            ttk.Combobox(
                self.fields_frame,
                textvariable=self.from_var,
                values=["Gallons (gal)", "Liters (L)"],
                state="readonly",
                width=15
            ).grid(row=1, column=1, padx=5, pady=5)

            ttk.Label(self.fields_frame, text="To:").grid(row=2, column=0, padx=5, pady=5)
            ttk.Combobox(
                self.fields_frame,
                textvariable=self.to_var,
                values=["Liters (L)", "Gallons (gal)"],
                state="readonly",
                width=15
            ).grid(row=2, column=1, padx=5, pady=5)

    def perform_conversion(self):
        try:
            value = float(self.input_entry.get())
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()

            if not from_unit or not to_unit:
                messagebox.showwarning("Warning", "Please select both 'From' and 'To' units")
                return

            conversion_type = self.conversion_type.get()
            result = 0.0

            if conversion_type == "weight":
                if "Pounds" in from_unit and "Kilograms" in to_unit:
                    result = pound_to_kg(value)
                elif "Kilograms" in from_unit and "Pounds" in to_unit:
                    result = kg_to_pound(value)
                else:
                    messagebox.showwarning("Warning", "Invalid unit combination for weight conversion")
                    return

            elif conversion_type == "height":
                if "Inches" in from_unit and "Meters" in to_unit:
                    result = inch_to_meter(value)
                elif "Meters" in from_unit and "Inches" in to_unit:
                    result = meter_to_inch(value)
                else:
                    messagebox.showwarning("Warning", "Invalid unit combination for height conversion")
                    return

            elif conversion_type == "temp":
                if "Fahrenheit" in from_unit and "Celsius" in to_unit:
                    result = fahrenheit_to_celsius(value)
                elif "Celsius" in from_unit and "Fahrenheit" in to_unit:
                    result = celsius_to_fahrenheit(value)
                else:
                    messagebox.showwarning("Warning", "Invalid unit combination for temperature conversion")
                    return

            elif conversion_type == "volume":
                if "Gallons" in from_unit and "Liters" in to_unit:
                    result = gallon_to_liter(value)
                elif "Liters" in from_unit and "Gallons" in to_unit:
                    result = liter_to_gallon(value)
                else:
                    messagebox.showwarning("Warning", "Invalid unit combination for volume conversion")
                    return

            self.result_label.config(text=f"Result: {result:.2f} {to_unit.split(' ')[0]}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
