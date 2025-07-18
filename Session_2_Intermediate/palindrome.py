import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('palindrome.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def is_palindrome(word):
    """
    Check if a given word or phrase is a palindrome.
    
    This function takes a string input and checks if it reads the same forwards
    and backwards after removing non-alphanumeric characters and converting to lowercase.
    It includes comprehensive logging to track intermediate processing steps.
    
    Args:
        word (str): The input string to check for palindrome properties
    
    Returns:
        bool: True if the input is a palindrome, False otherwise
    
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    logger.info(f"Starting palindrome check for input: '{word}'")
    logger.info(f"Input type: {type(word)}, Length: {len(word)}")
    
    try:
        # Step 1: Convert and validate input types
        logger.debug("Step 1: Converting input to string if needed")
        original_input = str(word) if not isinstance(word, str) else word
        logger.info(f"Original input after conversion: '{original_input}'")
        
        # Step 2: Clean the input (remove non-alphanumeric and convert to lowercase)
        logger.debug("Step 2: Cleaning input - removing non-alphanumeric characters and converting to lowercase")
        cleaned_chars = []
        for i, char in enumerate(original_input):
            if char.isalnum():
                cleaned_char = char.lower()
                cleaned_chars.append(cleaned_char)
                logger.debug(f"Character {i}: '{char}' -> '{cleaned_char}' (kept)")
            else:
                logger.debug(f"Character {i}: '{char}' -> removed (not alphanumeric)")
        
        cleaned = ''.join(cleaned_chars)
        logger.info(f"Cleaned string: '{cleaned}' (length: {len(cleaned)})")
        
        # Step 3: Handle edge cases
        if len(cleaned) == 0:
            logger.info("Empty string after cleaning - returning True (empty string is considered palindrome)")
            return True
        
        if len(cleaned) == 1:
            logger.info("Single character after cleaning - returning True (single character is palindrome)")
            return True
        
        # Step 4: Check if palindrome
        logger.debug("Step 4: Checking if cleaned string is palindrome")
        reversed_string = cleaned[::-1]
        logger.debug(f"Original cleaned: '{cleaned}'")
        logger.debug(f"Reversed string: '{reversed_string}'")
        
        is_palindrome_result = cleaned == reversed_string
        logger.info(f"Palindrome check result: {is_palindrome_result}")
        
        if is_palindrome_result:
            logger.info(f"[PALINDROME] '{word}' IS a palindrome (cleaned: '{cleaned}')")
        else:
            logger.info(f"[NOT PALINDROME] '{word}' is NOT a palindrome (cleaned: '{cleaned}')")
        
        return is_palindrome_result
        
    except Exception as e:
        logger.error(f"Error processing input '{word}': {str(e)}")
        logger.error(f"Error type: {type(e).__name__}")
        raise
