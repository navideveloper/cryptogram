import math

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(plain_text:str,key:tuple,alphabet=ALPHABET):
    logs = f'Matn: "{plain_text}"'
    a,b = key
    m = len(alphabet)
    cipher_text = ''
    if math.gcd(a,m) != 1:
        return "'a' kaliti va alifbo uzunligi 'm' o'zaro tub bo'lishi shart!"
    for char in plain_text.lower():
        if char in alphabet:
            x=alphabet.index(char)
            y=(a*x+b)%m
            logs += f"\n{char}({x}) → ({a}*{x}+{b}) mod {m} = {y} → {alphabet[y]}"
            cipher_text += alphabet[y]
        else:
            cipher_text += char
    logs += f'\n\nNatija: "{plain_text}" → "{cipher_text}"'
    return cipher_text,logs

def decrypt(cipher_text:str,key:tuple,alphabet=ALPHABET):
    logs = f'shifr: "{cipher_text}"'
    a,b = key
    m = len(alphabet)
    a_inverse = mod_inverse(a,m)
    logs += f'\nA invers: {a_inverse}'
    plain_text = ''
    if a_inverse is None:
        return "'a' kaliti ({a}) va alfavit uzunligi ({m}) o'zaro tub bo'lishi shart!"
    for char in cipher_text.lower():
        if char in alphabet:
            y=alphabet.index(char)
            x=((y-b)*a_inverse)%m
            logs += f"\n{char}({y}) → ({a_inverse}*{y}+{b}) mod {m} = {x} → {alphabet[x]}"
            plain_text += alphabet[x]
        else:
            plain_text += char
    logs += f'\n\nNatija: "{cipher_text}" → "{plain_text}"'
    return plain_text,logs

if __name__ == '__main__':
    c = encrypt('hello',(15,5),ALPHABET)
    p = decrypt(c,(15,5),ALPHABET)
    print('hello ->',c)
    print(c, '->', p)