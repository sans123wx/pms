from Crypto.Cipher import AES
import base64

def add_to_16(text):
    while len(text) % 16 != 0:
        text += '\0'
    return str.encode(text)

def encrypt(text , key):
    if type(text) == 'int':
        text = str(text)
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')
    return encrypted_text

def decrypt(encrypted_text , key):
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    decrypted_text = str(aes.decrypt(base64.decodebytes(bytes(encrypted_text, encoding='utf8'))).rstrip(b'\0').decode("utf8"))
    return decrypted_text
