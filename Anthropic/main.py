"""
This module provides a function to calculate pi to the 5th decimal place.
"""

def calculate_pi(decimal_places=5):
    """
    Calculate the value of pi to the specified number of decimal places
    using the Nilakantha series.
    
    Args:
        decimal_places (int): Number of decimal places to calculate (default is 5)
        
    Returns:
        float: Value of pi calculated to the specified decimal places
    """
    # We need more precision in our calculation than our final result
    # to ensure the 5th decimal is accurate
    target_precision = 10**(-(decimal_places + 2))
    
    # Start with the basic approximation of pi
    pi = 3.0
    
    # Nilakantha series: π = 3 + 4/(2×3×4) - 4/(4×5×6) + 4/(6×7×8) - ...
    addition = True  # Controls whether we add or subtract
    divisor = 2
    
    # Continue until we reach desired precision
    current_term = 1.0
    while abs(current_term) > target_precision:
        n1, n2, n3 = divisor, divisor + 1, divisor + 2
        current_term = 4.0 / (n1 * n2 * n3)
        
        if addition:
            pi += current_term
        else:
            pi -= current_term
            
        addition = not addition
        divisor += 2
    
    # Round to the desired number of decimal places
    return round(pi, decimal_places)


if __name__ == "__main__":
    # When run directly, calculate and display pi
    pi_value = calculate_pi()
    print(f"Pi calculated to 5 decimal places: {pi_value}")