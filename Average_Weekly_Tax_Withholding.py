def calculate_tax(income):
    if income < 500:
        return income * 0.10
    elif income < 1500:
        return income * 0.15
    elif income < 2500:
        return income * 0.20
    else:
        return income * 0.30

def main():
    incomes = [450, 1200, 1800, 2600]
    weeks = len(incomes)
    total_tax = 0

    print("Weekly Incomes and Tax Withheld:")
    for i, income in enumerate(incomes):
        tax = calculate_tax(income)
        total_tax += tax
        print(f"Week {i+1}: Income = ${income:.2f}, Tax = ${tax:.2f}")

    average_tax = total_tax / weeks
    print(f"\nAverage Weekly Tax Withholding: ${average_tax:.2f}")

if __name__ == "__main__":
    main()

