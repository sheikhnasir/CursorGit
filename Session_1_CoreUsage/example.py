def get_discounted_price(price, discount_percent):
    """
    Calculate the discounted price after applying a percentage discount.
    
    This function takes an original price and a discount percentage, then
    calculates the final price after applying the discount. It includes
    validation to handle edge cases like negative prices or discounts.
    
    Args:
        price (float): The original price of the item (must be positive)
        discount_percent (float): The discount percentage to apply (must be non-negative)
    
    Returns:
        float: The discounted price. Returns 0 if price <= 0 or discount_percent < 0
    
    Examples:
        >>> get_discounted_price(100, 20)
        80.0
        >>> get_discounted_price(50, 10)
        45.0
        >>> get_discounted_price(0, 15)
        0
        >>> get_discounted_price(100, -5)
        0
    """
    try:
        # Step 1: Convert and validate input types
        original_price = float(price)
        discount_rate = float(discount_percent)
        
        # Step 2: Validate business logic constraints
        if original_price <= 0:
            return 0  # Invalid price
        if discount_rate < 0:
            return 0  # Invalid discount rate
        
        # Step 3: Calculate the discount amount
        discount_amount = original_price * discount_rate / 100
        
        # Step 4: Calculate final price and ensure it's not negative
        final_price = original_price - discount_amount
        final_price = max(0, final_price)  # Prevent negative prices
        
        return final_price
        
    except (ValueError, TypeError):
        # Handle invalid input types (e.g., strings, None, etc.)
        return 0
    except ZeroDivisionError:
        # Handle division by zero (shouldn't occur with our logic)
        return original_price
    except Exception as unexpected_error:
        # Handle any other unexpected errors
        print(f"Unexpected error in get_discounted_price: {unexpected_error}")
        return 0
