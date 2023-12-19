def xor_recursivo(tp, chave, cifrado=None, indice=0):
  if cifrado is None:
      cifrado = []

  if indice < len(tp):
      byte_cifrado = tp[indice] ^ chave[indice % len(chave)]
      cifrado.append(byte_cifrado)
      return xor_recursivo(tp, chave, cifrado, indice + 1)
  else:
      return bytes(cifrado)


def xor_iterativo(texto_plano, chave):

  # returns plain text by repeatedly xoring it with chave
  tp = texto_plano
  len_chave = len(chave)
  cifrado = []

  for i in range(0, len(tp)):
    cifrado.append(tp[i] ^ chave[i % len_chave])
  return bytes(cifrado)

texto_plano = b'Esta e uma mensagem codificada com o algoritmo XOR'
chave = b'SenhaXOR'

print("Plain text: ", texto_plano)
print("Encrytped as: ", xor_recursivo(texto_plano, chave).hex())
print("decrytpion: ", xor_recursivo(xor_recursivo(texto_plano, chave), chave).decode()) 
