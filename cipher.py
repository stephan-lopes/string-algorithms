import string

def cypher(s1: str, key: int) -> str:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase

    encrypt = ''

    for c in s1:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]

    return encrypt