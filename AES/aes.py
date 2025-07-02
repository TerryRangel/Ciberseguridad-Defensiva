from Crypto.Cipher import AES

clave_cifrado=b'A\x83\xbeU\xd7\xa9b\x18\x85AN0\xbft\xc3\xab'
texto_plano=b'texto secreto'

AES_cypher= AES.new(clave_cifrado, AES.MODE_ECB)
#PREGUNTA 1
while len(texto_plano) % 16 != 0:
    texto_plano += b'\x00'  # Padding to 16 bytes
texto_cifrado = AES_cypher.encrypt(texto_plano) 
print(f'Texto cifrado: {texto_cifrado},Texto plano: {texto_plano}')


#PREGUNTA 2
texto_plano=b'texto secreto'
AES_cipher = AES.new(clave_cifrado, AES.MODE_CTR)
texto_cifrado = AES_cipher.encrypt(texto_plano)
print(f'Texto cifrado Modo de Operacion CTR: {texto_cifrado},Texto plano: {texto_plano}')

#Pregunta 4
texto_cifrado_ECB=b'\xd5\x8b\xc2\xd0F\xc0w\xfe\xc1\x12\xaaX\x8f}{)i[\xf1\xc7\x9d\x1d\x08\xcd\xc2\xd8>;\r\xef\xce\xec\x89\xbd\xeb{\xe6mY\xcev\xb9\xdb\x06\x17\xd9\xd6cG6\xb4\xcfN\xf9\x15.\xbe\xed\xe7\xee#\xd0\xd9\x03\xb9l\xbap\x0c\x9c\xbe\xc3\xe1\xae\x86~pk\\\x0f'
clave_cifrado=b'A\x83\xbeU\xd7\xa9b\x18\x85AN0\xbft\xc3\xab'
AES_cypher = AES.new(clave_cifrado, AES.MODE_ECB)
texto_plano = AES_cypher.decrypt(texto_cifrado_ECB)
print(f'Texto plano descifrado MODE ECB: {texto_plano}')

parte=b"\x1fX\xba(\\X\xe6E{(}\x8a}d}0"

from Crypto.Util import Counter
texto_cifrado_CTR= b'{\x9a`\x04\x80\xc5\x026D\x1f\xaf\x9c&\xd1\x83\x0c\xf2wL\xd6F}\xd35B.\xb4\xe5\xb1^\x05 P\xc8\xe8\x89\xe1\xf7;G\x13\xf0\xccbs\xe8\x121\x8b4\xbf\xda\x93v\xcb\xe4\xf8g\xe72\xc5~\x97\x01TR\x9d\x0b'
AES_cipher = AES.new(clave_cifrado, AES.MODE_CTR,counter=Counter.new(128))
texto_plano = AES_cipher.decrypt(texto_cifrado_CTR)
print(f'Texto plano descifrado MODE CTR: {texto_plano}' )