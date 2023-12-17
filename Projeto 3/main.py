def recursive_xor(pt, key, encoded=None, index=0):
  if encoded is None:
      encoded = []

  if index < len(pt):
      encoded_byte = pt[index] ^ key[index % len(key)]
      encoded.append(encoded_byte)
      return recursive_xor(pt, key, encoded, index + 1)
  else:
      return bytes(encoded)



plain_text = b'Esta e uma mensagem codificada com o algoritmo XOR'
key = b'SenhaXOR'

print("Plain text: ", plain_text)
print("Encrypted as: ", recursive_xor(plain_text, key).hex())
print("decryption: ", recursive_xor(recursive_xor(plain_text, key), key).decode()) 
