import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from string_utils import (
    reverse_string,
    capitalize_words,
    count_vowels,
    is_palindrome,
)

# ────────────────────────────────────────────────────────────────────────────────
# reverse_string
# ────────────────────────────────────────────────────────────────────────────────
assert reverse_string("") == ""
assert reverse_string("a") == "a"
assert reverse_string("abcd") == "dcba"
assert reverse_string("123 😊 abc") == "cba 😊 321"

# ────────────────────────────────────────────────────────────────────────────────
# capitalize_words
# ────────────────────────────────────────────────────────────────────────────────
assert capitalize_words("") == ""
assert capitalize_words("hello world") == "Hello World"
assert capitalize_words("  multiple   spaces ") == "Multiple Spaces"
assert capitalize_words("mIxEd cAsE") == "Mixed Case"
assert capitalize_words("naïve café") == "Naïve Café"

# ────────────────────────────────────────────────────────────────────────────────
# count_vowels
# ────────────────────────────────────────────────────────────────────────────────
assert count_vowels("") == 0
assert count_vowels("bcdfg") == 0
assert count_vowels("aeiou") == 5
assert count_vowels("AEIOU") == 5
assert count_vowels("Hello, world!") == 3          # e, o, o
assert count_vowels("Пайтон") == 0                 # Cyrillic letters not in vowel set

# ────────────────────────────────────────────────────────────────────────────────
# is_palindrome
# ────────────────────────────────────────────────────────────────────────────────
assert is_palindrome("") is True
assert is_palindrome("a") is True
assert is_palindrome("racecar") is True
assert is_palindrome("RaceCar") is False
assert is_palindrome("A man, a plan, a canal: Panama") is False
assert is_palindrome("not a palindrome") is False
