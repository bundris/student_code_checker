def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def count_vowels(s):
    vowels = 'euioaEUIOA'
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    normalized = ''.join(c for c in s if c.isalnum())
    return normalized == normalized[::-1]
