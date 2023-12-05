# Get input from the user
current_fuel_price = float(input("Enter current fuel price per liter in rupees: "))
distance_traveled = float(input("Enter dist traveled in kilometers: "))
car_mileage = float(input("Enter car mileage in kilometers per liter: "))

# Check for valid inputs
if current_fuel_price <= 0 or distance_traveled <= 0 or car_mileage <= 0:
    print("Inputs must be positive numbers.")
else:
    # Calculate and display the fuel cost
    fuel_required = distance_traveled / car_mileage
    total_cost = fuel_required * current_fuel_price
    print(f"The fuel cost for the trip is: {total_cost:.2f} rupees.")
