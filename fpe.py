from ff3 import FF3Cipher
import random
import secrets

key = secrets.token_hex(16)
tweak = "D8E7920AFA330A73"
c = FF3Cipher(key, tweak)

#plaintext = "1234567890123456"
plaintext = input("enter the value:")
ciphertext = c.encrypt(plaintext)
decrypted = c.decrypt(ciphertext)

print(f"{plaintext} -> {ciphertext} -> {decrypted}" )

# format encrypted value
CT = f"{ciphertext[:4]} {ciphertext[4:8]} {ciphertext[8:12]} {ciphertext[12:]}"
print(f"Encrypted value after formatting: {CT}")

