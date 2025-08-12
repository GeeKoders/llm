"""
This module tests the calculate_pi function from the main module.
"""

import unittest
from main import calculate_pi

class TestPiCalculation(unittest.TestCase):
    """Test cases for the calculate_pi function."""
    
    def test_pi_default_precision(self):
        """Test that the default precision (5 decimal places) is correct."""
        pi_value = calculate_pi()
        # The value of pi to 5 decimal places is 3.14159
        self.assertEqual(pi_value, 3.14159)
    
    def test_pi_different_precision(self):
        """Test that different precision values work correctly."""
        # Test with 3 decimal places
        self.assertEqual(calculate_pi(3), 3.142)
        
        # Test with 7 decimal places
        self.assertEqual(calculate_pi(7), 3.1415927)
    
    def test_pi_type(self):
        """Test that the function returns a float."""
        self.assertIsInstance(calculate_pi(), float)


if __name__ == "__main__":
    unittest.main()