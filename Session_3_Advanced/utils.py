def validate_numeric_input(value, field_name):
    """
    Validate that a value is numeric and can be converted to float.
    
    Args:
        value: The value to validate
        field_name (str): Name of the field for error messages
    
    Returns:
        float: The converted float value, or None if invalid
    
    Examples:
        >>> validate_numeric_input(1.75, "height")
        1.75
        >>> validate_numeric_input("abc", "height")
        None
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        print(f"Error: {field_name} must be a numeric value, got {value}")
        return None


def validate_positive_value(value, field_name):
    """
    Validate that a value is positive (greater than 0).
    
    Args:
        value (float): The value to validate
        field_name (str): Name of the field for error messages
    
    Returns:
        bool: True if valid, False if invalid
    
    Examples:
        >>> validate_positive_value(1.75, "height")
        True
        >>> validate_positive_value(0, "height")
        False
    """
    if value <= 0:
        print(f"Error: {field_name} must be positive, got {value}")
        return False
    return True


def validate_bmi_inputs(height, weight):
    """
    Validate both height and weight inputs for BMI calculation.
    
    Args:
        height: Height value to validate
        weight: Weight value to validate
    
    Returns:
        tuple: (validated_height, validated_weight) or (None, None) if invalid
    
    Examples:
        >>> validate_bmi_inputs(1.75, 70)
        (1.75, 70.0)
        >>> validate_bmi_inputs(0, 70)
        (None, None)
    """
    # Validate numeric inputs
    validated_height = validate_numeric_input(height, "height")
    if validated_height is None:
        return None, None
    
    validated_weight = validate_numeric_input(weight, "weight")
    if validated_weight is None:
        return None, None
    
    # Validate positive values
    if not validate_positive_value(validated_height, "height"):
        return None, None
    
    if not validate_positive_value(validated_weight, "weight"):
        return None, None
    
    return validated_height, validated_weight


def calculate_bmi(height, weight):
    """
    Calculate Body Mass Index (BMI) with separated validation logic.
    
    Args:
        height (float): Height in meters (must be positive)
        weight (float): Weight in kilograms (must be positive)
    
    Returns:
        float: BMI value rounded to 2 decimal places, or None if invalid input
    
    Examples:
        >>> calculate_bmi(1.75, 70)
        22.86
        >>> calculate_bmi(0, 70)
        None
        >>> calculate_bmi(1.75, -5)
        None
    """
    try:
        # Validate inputs using separated validation logic
        validated_height, validated_weight = validate_bmi_inputs(height, weight)
        
        if validated_height is None or validated_weight is None:
            return None
        
        # Calculate BMI: weight (kg) / height (m)²
        bmi = validated_weight / (validated_height ** 2)
        
        # Return rounded result
        return round(bmi, 2)
        
    except Exception as e:
        print(f"Unexpected error calculating BMI: {e}")
        return None
