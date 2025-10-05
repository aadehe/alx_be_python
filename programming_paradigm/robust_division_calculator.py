def safe_divide(numerator, denominator):
    """Performs division and handles division by zero."""
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Non-numeric input is not allowed."
    return result
