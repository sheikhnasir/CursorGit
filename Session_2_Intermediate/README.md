# Session 2: Intermediate Python Concepts

## Palindrome Checker

This session demonstrates intermediate Python concepts including string manipulation, list comprehensions, and efficient algorithms.

### Files
- `palindrome.py` - Contains the palindrome checking function

## Function Documentation

### `is_palindrome(word)`

**Purpose:** Checks if a given word or phrase is a palindrome (reads the same forwards and backwards).

**Parameters:**
- `word` (str): The input string to check for palindrome properties

**Returns:**
- `bool`: `True` if the input is a palindrome, `False` otherwise

**Algorithm:**
1. **Text Cleaning:** Removes all non-alphanumeric characters and converts to lowercase
2. **Palindrome Check:** Compares the cleaned string with its reverse

**Code Implementation:**
```python
def is_palindrome(word):
    cleaned = ''.join(c.lower() for c in word if c.isalnum())
    return cleaned == cleaned[::-1]
```

## Features

### ✅ Case Insensitive
The function ignores letter case when checking palindromes.

**Examples:**
- `"Racecar"` → `True`
- `"RACECAR"` → `True`
- `"racecar"` → `True`

### ✅ Ignores Punctuation and Spaces
Removes all non-alphanumeric characters before checking.

**Examples:**
- `"A man, a plan, a canal: Panama"` → `True`
- `"Was it a car or a cat I saw?"` → `True`
- `"Madam, I'm Adam"` → `True`

### ✅ Handles Numbers
Works with numeric palindromes as well.

**Examples:**
- `"12321"` → `True`
- `"12345"` → `False`

## Usage Examples

```python
# Basic palindromes
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False

# Complex phrases
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("Was it a car or a cat I saw?"))    # True

# Numbers
print(is_palindrome("12321"))    # True
print(is_palindrome("12345"))    # False

# Edge cases
print(is_palindrome(""))         # True (empty string)
print(is_palindrome("a"))        # True (single character)
print(is_palindrome("123 321"))  # True (with spaces)
```

## Technical Details

### String Processing
- Uses `c.lower()` to convert characters to lowercase
- Uses `c.isalnum()` to filter only alphanumeric characters
- Uses list comprehension for efficient processing

### Palindrome Detection
- Uses Python's slice notation `[::-1]` for string reversal
- Compares original cleaned string with its reverse
- Returns boolean result of the comparison

### Performance
- **Time Complexity:** O(n) where n is the length of the input string
- **Space Complexity:** O(n) for storing the cleaned string

## Learning Objectives

This example demonstrates:
1. **String Manipulation:** Converting case, filtering characters
2. **List Comprehensions:** Efficient character processing
3. **Slice Notation:** String reversal with `[::-1]`
4. **Algorithm Design:** Simple yet effective palindrome detection
5. **Edge Case Handling:** Empty strings, single characters, mixed content

## Testing

You can test the function with various inputs:

```python
test_cases = [
    "racecar",
    "A man, a plan, a canal: Panama",
    "hello",
    "12321",
    "Was it a car or a cat I saw?",
    "",
    "a",
    "Madam, I'm Adam"
]

for test in test_cases:
    result = is_palindrome(test)
    print(f'"{test}" → {result}')
```

## Next Steps

Consider extending this function to:
- Handle Unicode characters
- Add performance optimizations
- Create a case-sensitive version
- Add support for different palindrome types (word-level vs character-level) 