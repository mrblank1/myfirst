import hashlib
a='12345654321'.encode()
print(hashlib.sha256(a).hexdigest().upper())