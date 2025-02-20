#Drake Pierce-Demksi
#

# Global conversion constants
POUND_TO_KG = 0.453592
INCH_TO_METER = 0.0254

def bmi_calculation():
    try:
        # User input
        weight_pounds = float(input("Enter your weight in pounds: "))
        height_inches = float(input("Enter your height in inches: "))

        # Convert to metric
        weight_kg = weight_pounds * POUND_TO_KG
        height_m = height_inches * INCH_TO_METER

        # BMI calculation
        bmi = weight_kg / (height_m ** 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        # Output
        print(f"Your BMI is {bmi:.2f}")
        print(f"BMI category: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    bmi_calculation()
