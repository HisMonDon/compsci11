"""
What you should do
In the main function, make the item_price a negative number. i.e., -2.99. Run the program and explain what happens. Answer the following in a comment.

What is the error?
The error is that the price cannot be negative

What is the message?
The message is Price Cannot be negative

On what line does the error occur?
Line 43

What caused the error?
The price is negative, so the code raised the ValueError that the price cannot be negative

In the calc_subtotal function, add a check for the quantity value. Quantities cannot be negative so also raise a ValueError if the quantity is negative. In the main function fix the item_price variable to make it positive and make the quantity negative to observe the error.

In the main function, make both item_price and quantity negative. What do you see and what do you not see. Explain in a comment.
I only see the quantity value error, and not the price value error, because the quantity value error stops the code before it reaches the price value error.

"""



def main():
    item_price = -2.99
    quantity = -3
    print(f"{quantity} items at ${item_price} each is:")
    print(f"${calc_subtotal(item_price, quantity)}")


def calc_subtotal(price: float, quantity: int) -> float:
    """Calculate the subtotal for a single item in a cart.
    
    Args:
        price: The price of a single item.
        quantity: Number of a particular item in the cart.
    
    Returns:
        The subtotal
    """
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    if price < 0:
        raise ValueError("Price cannot be negative.")

    return price * quantity


if __name__ == "__main__":
    main()
