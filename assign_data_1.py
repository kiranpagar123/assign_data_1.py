# Assuming you have a dataframe or dataset with a 'ship_mode', 'sales', and 'profit' column

def calculate_surcharge(ship_mode, sales, profit):
    if ship_mode == "Same Day":
        surcharge = 0.2
    elif ship_mode == "First Class":
        surcharge = 0.1
    elif ship_mode == "Standard Class":
        surcharge = 0.05
    else:
        surcharge = 0

    total_cost = (sales - profit) * (1 + surcharge)
    return total_cost

# Example usage
ship_mode = "Same Day"
sales = 1000
profit = 200

total_cost = calculate_surcharge(ship_mode, sales, profit)
print(f"Total cost: {total_cost}")
