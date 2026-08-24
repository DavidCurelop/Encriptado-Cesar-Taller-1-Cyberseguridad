def cifrar(clave, texto):
    cifrado = ''
    if not isinstance(texto, str):
        return cifrado
    for ch in texto:
        code = ord(ch)
        # lowercase
        if 97 <= code <= 122:
            cifrado += chr((code - 97 + clave) % 26 + 97)
        # uppercase
        elif 65 <= code <= 90:
            cifrado += chr((code - 65 + clave) % 26 + 65)
        else:
            cifrado += ch
    return cifrado

def descifrar(clave, texto):
    descifrado = ''
    if not isinstance(texto, str):
        return descifrado
    for ch in texto:
        code = ord(ch)
        # lowercase
        if 97 <= code <= 122:
            descifrado += chr((code - 97 - clave) % 26 + 97)
        # uppercase
        elif 65 <= code <= 90:
            descifrado += chr((code - 65 - clave) % 26 + 65)
        else:
            descifrado += ch
    return descifrado
