def is_palindrome(word):
    """Return True if word is a palindrome (case-insensitive)."""
    cleaned = word.lower()
    return cleaned == cleaned[::-1]

def find_palindromes(words):
    """Return a list of palindromic words from the given list."""
    palindromes = []
    for word in words:
        if is_palindrome(word):
            palindromes.append(word)
    return palindromes