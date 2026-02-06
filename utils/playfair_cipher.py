import string

ALPHABET = [
    ['A','B','C','D','E'],
    ['F','G','H','I/J','K'],
    ['L','M','N','O','P'],
    ['Q','R','S','T','U'],
    ['V','W','X','Y','Z'],
]

def square(keyword: str):
    keyword = keyword.upper().replace("J", "I")
    seen = set()
    square = []
    for ch in keyword:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            square.append(ch)
    for ch in string.ascii_uppercase:
        if ch == "J":
            continue
        if ch not in seen:
            seen.add(ch)
            square.append(ch)

    return [square[i:i+5] for i in range(0, 25, 5)]

def find_position(square, ch):
    for r in range(5):
        for c in range(5):
            if ch == square[r][c]:
                return r, c

def encrypt(plain_text: str, keyword: str=''):
    if not plain_text:
        return ''
    square_matrix = square(keyword)

    plain_text = plain_text.upper().replace("J", "I")
    plain_text = ''.join(ch for ch in plain_text if ch.isalpha())

    pairs = []
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        b = plain_text[i+1] if i+1 < len(plain_text) else 'X'
        if a == b:
            pairs.append((a, 'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2

    cipher_text = ""
    for a, b in pairs:
        r1, c1 = find_position(square_matrix, a)
        r2, c2 = find_position(square_matrix, b)

        if r1 == r2:
            cipher_text += square_matrix[r1][(c1 + 1) % 5]
            cipher_text += square_matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            cipher_text += square_matrix[(r1 + 1) % 5][c1]
            cipher_text += square_matrix[(r2 + 1) % 5][c2]

        else:
            cipher_text += square_matrix[r1][c2]
            cipher_text += square_matrix[r2][c1]

    return cipher_text

def decrypt(cipher_text: str, keyword: str=''):
    if not cipher_text or len(cipher_text.replace(' ','')) % 2 != 0:
        return ''
    square_matrix = square(keyword)

    cipher_text = cipher_text.upper()
    cipher_text = ''.join(ch for ch in cipher_text if ch.isalpha())
    plain_text = ""

    for i in range(0, len(cipher_text), 2):
        a = cipher_text[i]
        b = cipher_text[i+1]

        r1, c1 = find_position(square_matrix, a)
        r2, c2 = find_position(square_matrix, b)

        if r1 == r2:
            plain_text += square_matrix[r1][(c1 - 1) % 5]
            plain_text += square_matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:
            plain_text += square_matrix[(r1 - 1) % 5][c1]
            plain_text += square_matrix[(r2 - 1) % 5][c2]

        else:
            plain_text += square_matrix[r1][c2]
            plain_text += square_matrix[r2][c1]

    return plain_text
