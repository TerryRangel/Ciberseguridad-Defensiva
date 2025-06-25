from Crypto.Cipher import ChaCha20

# =======================
# Parte 1: CIFRADO O
# =======================
clave_cifrado = b'z\xe8~"\xcayW\x14g\x18+\x1c+\xf9\x80\x06P\x9ej\x888\xb4G\xdf\xe4\xc50,\x8dY\x80\x19'
nonce = b'\xd6\x7f6\xc7\xe8i*\xa4'
texto_plano = b"Este es un mensaje secreto que quiero cifrar."

# Cifrar el texto
cifrador = ChaCha20.new(key=clave_cifrado, nonce=nonce)
texto_cifrado = cifrador.encrypt(texto_plano)
print("Texto cifrado (nuevo):", texto_cifrado)

# Parte 2: DESCIFRADO USANDO TEXTO CIFRADO
texto_cifrado= b'Ehq0\x83\xcb\x8fo\xab\xed\xd0S\x06\xcc\xbb\xecw\xe9\xec(\x1f\xc5E\xdb\x88\x18`W\xc3yQn\xad3\xec.\x08\x92\x8d\x8e\xbb%\x8f\x1a\xa6\xc9=\x15\x0f5\xaa'
descifrador = ChaCha20.new(key=clave_cifrado, nonce=nonce)
texto_descifrado = descifrador.decrypt(texto_cifrado)
print("Texto descifrado:", texto_descifrado.decode())



# Parte 3: DESCIFRADO CON PERDIDAD DE BYTES
texto_cifrado_perdido = b"\xad\xe2\x9a[C\xca\xa9\xadn\xf9\xaa)\x13\xc2X\x9e\x89\x19`C\xc4n\x1em\xf8?\xe7|\x0b\xd3\xdc\x8f\xacd\x85\x0c\xb8\xc3'\x1a\x12>"
descifrador.seek(8)
texto_descifrado_perdido = descifrador.decrypt(texto_cifrado_perdido)
print("Texto descifrado con bytes perdidos:", texto_descifrado_perdido.decode(errors='ignore'))