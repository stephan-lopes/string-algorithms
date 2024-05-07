def is_palindrome(s1: str) -> bool:
    if s1.lower() == s1[::-1].lower():
        return True
    return False

if __name__ == "__main__":
    print(is_palindrome("kayak"))