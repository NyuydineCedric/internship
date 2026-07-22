#PALINDROME CHECKER
def is_palindrome(word):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_word = ''.join(c.lower() for c in word if c.isalnum())
    # Check if the cleaned word is equal to its reverse
    return cleaned_word == cleaned_word[::-1]

def find_palindromes(words):
    palindromes = []
    for word in words:
        if is_palindrome(word):
            palindromes.append(word)
    return palindromes

result = find_palindromes(["level", "radar", "hello", "madam","nice", "world", "civic"])
print("Palindromic words:", result)