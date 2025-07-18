#!/usr/bin/env python3
"""
Test script to demonstrate logging functionality of the palindrome function.
This script shows how the logging tracks intermediate steps during palindrome checking.
"""

from palindrome import is_palindrome
import logging

def test_logging_examples():
    """Test various inputs to demonstrate logging functionality."""
    
    print("=" * 60)
    print("PALINDROME FUNCTION LOGGING DEMONSTRATION")
    print("=" * 60)
    
    # Test cases to demonstrate different logging scenarios
    test_cases = [
        "racecar",
        "A man, a plan, a canal: Panama",
        "hello",
        "12321",
        "Was it a car or a cat I saw?",
        "python",
        "Madam, I'm Adam",
        "!@#$%",
        "a",
        ""
    ]
    
    for i, test_input in enumerate(test_cases, 1):
        print(f"\n{'='*20} TEST {i}: '{test_input}' {'='*20}")
        
        try:
            result = is_palindrome(test_input)
            print(f"\nFINAL RESULT: {result}")
        except Exception as e:
            print(f"ERROR: {e}")
        
        print("-" * 60)

def test_debug_logging():
    """Test with debug logging enabled to see detailed character processing."""
    
    print("\n" + "=" * 60)
    print("DEBUG LOGGING DEMONSTRATION")
    print("=" * 60)
    
    # Enable debug logging
    logging.getLogger().setLevel(logging.DEBUG)
    
    test_input = "Race, car!"
    print(f"\nTesting with debug logging: '{test_input}'")
    
    try:
        result = is_palindrome(test_input)
        print(f"\nFINAL RESULT: {result}")
    except Exception as e:
        print(f"ERROR: {e}")
    
    # Reset to INFO level
    logging.getLogger().setLevel(logging.INFO)

def show_log_file_info():
    """Show information about the log file."""
    print("\n" + "=" * 60)
    print("LOG FILE INFORMATION")
    print("=" * 60)
    
    try:
        with open('palindrome.log', 'r') as f:
            log_content = f.read()
            print(f"Log file 'palindrome.log' contains {len(log_content)} characters")
            print(f"Number of log entries: {log_content.count(' - INFO -') + log_content.count(' - DEBUG -') + log_content.count(' - ERROR -')}")
            
            print("\nLast 5 log entries:")
            lines = log_content.strip().split('\n')
            for line in lines[-5:]:
                print(f"  {line}")
                
    except FileNotFoundError:
        print("Log file 'palindrome.log' not found yet.")
    except Exception as e:
        print(f"Error reading log file: {e}")

if __name__ == "__main__":
    # Run the logging demonstrations
    test_logging_examples()
    test_debug_logging()
    show_log_file_info()
    
    print("\n" + "=" * 60)
    print("LOGGING DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("Check 'palindrome.log' file for detailed logging information.")
    print("=" * 60) 