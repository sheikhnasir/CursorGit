import pytest
from palindrome import is_palindrome


class TestPalindrome:
    """Test cases for the is_palindrome function."""

    def test_basic_palindromes(self):
        """Test basic palindrome words."""
        assert is_palindrome("racecar") == True
        assert is_palindrome("level") == True
        assert is_palindrome("deed") == True
        assert is_palindrome("radar") == True

    def test_non_palindromes(self):
        """Test words that are not palindromes."""
        assert is_palindrome("hello") == False
        assert is_palindrome("python") == False
        assert is_palindrome("world") == False
        assert is_palindrome("programming") == False

    def test_case_insensitive(self):
        """Test that the function is case insensitive."""
        assert is_palindrome("Racecar") == True
        assert is_palindrome("RACECAR") == True
        assert is_palindrome("RaCeCaR") == True
        assert is_palindrome("LEVEL") == True
        assert is_palindrome("Level") == True

    def test_with_punctuation_and_spaces(self):
        """Test palindromes with punctuation and spaces."""
        assert is_palindrome("A man, a plan, a canal: Panama") == True
        assert is_palindrome("Was it a car or a cat I saw?") == True
        assert is_palindrome("Madam, I'm Adam") == True
        assert is_palindrome("Do geese see God?") == True
        assert is_palindrome("Never odd or even") == True

    def test_numeric_palindromes(self):
        """Test numeric palindromes."""
        assert is_palindrome("12321") == True
        assert is_palindrome("1234321") == True
        assert is_palindrome("12345") == False
        assert is_palindrome("123321") == True

    def test_mixed_alphanumeric(self):
        """Test strings with both letters and numbers."""
        assert is_palindrome("race12321car") == False
        assert is_palindrome("12321race") == False
        assert is_palindrome("a1a") == True
        assert is_palindrome("1a1") == True

    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        assert is_palindrome("") == True  # Empty string
        assert is_palindrome("a") == True  # Single character
        assert is_palindrome("aa") == True  # Two same characters
        assert is_palindrome("ab") == False  # Two different characters

    def test_special_characters_only(self):
        """Test strings with only special characters."""
        assert is_palindrome("!@#$%") == True  # Empty after cleaning
        assert is_palindrome("   ") == True  # Only spaces
        assert is_palindrome(".,;:") == True  # Only punctuation

    def test_unicode_characters(self):
        """Test with Unicode characters."""
        assert is_palindrome("été") == True  # French word
        assert is_palindrome("anna") == True  # Common name
        assert is_palindrome("civic") == True  # English word

    def test_long_palindromes(self):
        """Test longer palindrome phrases."""
        long_palindrome = "Able was I ere I saw Elba"
        assert is_palindrome(long_palindrome) == True
        
        long_non_palindrome = "This is not a palindrome at all"
        assert is_palindrome(long_non_palindrome) == False

    def test_numbers_with_spaces(self):
        """Test numeric palindromes with spaces."""
        assert is_palindrome("123 321") == True
        assert is_palindrome("1 2 3 2 1") == True
        assert is_palindrome("123 456") == False

    def test_mixed_case_with_punctuation(self):
        """Test mixed case with punctuation."""
        assert is_palindrome("Race, car!") == True  # Becomes "racecar" after cleaning
        assert is_palindrome("A man, a plan, a canal: Panama") == True
        assert is_palindrome("Was it a car or a cat I saw?") == True

    @pytest.mark.parametrize("input_str,expected", [
        ("racecar", True),
        ("hello", False),
        ("12321", True),
        ("", True),
        ("a", True),
        ("A man, a plan, a canal: Panama", True),
        ("Was it a car or a cat I saw?", True),
        ("python", False),
        ("12345", False),
        ("Madam, I'm Adam", True),
    ])
    def test_parametrized_palindromes(self, input_str, expected):
        """Test multiple inputs using parametrization."""
        assert is_palindrome(input_str) == expected

    def test_function_returns_boolean(self):
        """Test that the function always returns a boolean."""
        result_true = is_palindrome("racecar")
        result_false = is_palindrome("hello")
        
        assert isinstance(result_true, bool)
        assert isinstance(result_false, bool)
        assert result_true == True
        assert result_false == False

    def test_no_side_effects(self):
        """Test that the function doesn't modify the input."""
        original_input = "Racecar"
        input_copy = original_input
        is_palindrome(original_input)
        
        assert original_input == input_copy  # Input should remain unchanged


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 