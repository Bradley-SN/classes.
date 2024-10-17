# Define the function to calculate the discounted price
def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount."""
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function and store the final price
    final_price = calculate_discount(price, discount_percent)

    # Print the appropriate message
    if final_price < price:
        print(f"The final price after applying the discount is: {final_price}")
    else:
        print(f"No discount applied. The original price is: {price}")

except ValueError:
    print("Invalid input. Please enter valid numbers for price and discount percentage.")
