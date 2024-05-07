
def is_anagram(s1: str, s2: str) -> bool:
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if sorted(s1) == sorted(s2):
        return True
    
    return False


if __name__ == "__main__":
    print(is_anagram("batata", "tabata"))