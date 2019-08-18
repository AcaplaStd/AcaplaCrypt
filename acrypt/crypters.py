from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from .utils import b64_to_random, random_to_b64


class RandomCrypter:
    def __init__(self, key: str):
        self._password = pad(key.encode('utf-8'), AES.block_size)

    def encode(self, data: str) -> str:
        iv = get_random_bytes(16)
        cipher = AES.new(self._password, AES.MODE_CBC, iv)
        ct = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
        res = b64encode(iv + ct).decode('utf-8')
        return b64_to_random(res)

    def decode(self, enc_data: str) -> str:
        iv_ct = b64decode(random_to_b64(enc_data))
        iv = iv_ct[:16]
        ct = iv_ct[16:]
        cipher = AES.new(self._password, AES.MODE_CBC, iv)
        res = unpad(cipher.decrypt(ct), AES.block_size)
        return res.decode('utf-8')


__all__ = ['RandomCrypter']
