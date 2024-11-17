ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"

def is_alpha(word):
    # Check if all characters in the word are in ASCII_LOWERCASE or ASCII_UPPERCASE
    for char in word:
        if char not in ASCII_LOWERCASE and char not in ASCII_UPPERCASE:
            return False
    return True

def is_digit(s):
    # Check if all characters in the string are in DECIMAL_DIGITS
    for char in s:
        if char not in DECIMAL_DIGITS:
            return False
    return True

def to_lower(s):
    # Convert all characters in the string to lowercase
    result = ""
    for char in s:
        if char in ASCII_UPPERCASE:
            result += ASCII_LOWERCASE[ASCII_UPPERCASE.index(char)]
        else:
            result += char
    return result

def to_upper(s):
    # Convert all characters in the string to uppercase
    result = ""
    for char in s:
        if char in ASCII_LOWERCASE:
            result += ASCII_UPPERCASE[ASCII_LOWERCASE.index(char)]
        else:
            result += char
    return result

def find_chr(s, char):
    # Find the index of the first occurrence of the character in the string
    for i in range(len(s)):
        if s[i] == char:
            return i
    return -1

def find_str(s, substr):
    # Find the index of the first occurrence of the substring in the string
    for i in range(len(s) - len(substr) + 1):
        match = True
        for j in range(len(substr)):
            if s[i + j] != substr[j]:
                match = False
                break
        if match:
            return i
    return -1

def replace_chr(s, old, new):
    # Replace all occurrences of the old character with the new character
    result = ""
    for char in s:
        if char == old:
            result += new
        else:
            result += char
    return result

def replace_str(s, old, new):
    # Replace all occurrences of the old substring with the new substring
    result = ""
    i = 0
    while i < len(s):
        if s[i:i + len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result
