import csv

# Function to calculate income tax based on income details
def calculate_income_tax(income_details):
    # Your income tax calculation logic here
    total_income = sum(income_details.values())
    # Sample calculation logic (simplified for demonstration)
    tax_rate = 0.20  # Assuming a flat tax rate for demonstration
    income_tax = total_income * tax_rate
    return income_tax

# Function to calculate pension contribution relief
def calculate_pension_relief(pension_contribution):
    # Your pension relief calculation logic here
    # Sample calculation logic (simplified for demonstration)
    relief_rate = 0.25  # Assuming a flat relief rate for demonstration
    pension_relief = pension_contribution * relief_rate
    return pension_relief

# Function to calculate Capital Gains Tax
def calculate_cgt(disposal_proceeds, acquisition_cost):
    # Your CGT calculation logic here
    # Sample calculation logic (simplified for demonstration)
    cgt_rate = 0.10  # Assuming a flat CGT rate for demonstration
    cgt = (disposal_proceeds - acquisition_cost) * cgt_rate
    return cgt

# Function to generate tax return
def generate_tax_return(income_tax, pension_relief, cgt):
    # Your tax return generation logic here
    # Sample tax return generation (simplified for demonstration)
    tax_return = {
        'Income Tax': income_tax,
        'Pension Contribution Relief': pension_relief,
        'Capital Gains Tax': cgt
    }
    return tax_return

# Function to save tax return summary as a CSV file
def save_tax_return_summary(tax_return, file_path):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = tax_return.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(tax_return)

# Function to submit RTI report
def submit_rti_report():
    # Your RTI reporting logic here
    # Sample RTI reporting logic (simplified for demonstration)
    print("RTI report submitted successfully.")

# Main function to orchestrate the tax preparation process
def tax_preparation_assistance():
    # Input gathering
    income_details = {
        'employment_income': float(input("Enter your employment income: ")),
        'self_employment_income': float(input("Enter your self-employment income: ")),
        'rental_income': float(input("Enter your rental income: "))
    }
    pension_contribution = float(input("Enter your pension contribution: "))
    disposal_proceeds = float(input("Enter disposal proceeds: "))
    acquisition_cost = float(input("Enter acquisition cost: "))

    # Tax calculation
    income_tax = calculate_income_tax(income_details)
    pension_relief = calculate_pension_relief(pension_contribution)
    cgt = calculate_cgt(disposal_proceeds, acquisition_cost)

    # Tax return generation
    tax_return = generate_tax_return(income_tax, pension_relief, cgt)
    print("\nTax Return Summary:")
    for key, value in tax_return.items():
        print(f"{key}: £{value:.2f}")

    # Save tax return summary as CSV
    save_tax_return_summary(tax_return, 'tax_return_summary.csv')

    # Submit RTI report
    submit_rti_report()

# Execute the tax preparation assistance function
tax_preparation_assistance()
