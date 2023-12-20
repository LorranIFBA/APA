from random import shuffle


def mergeSort(lista):
  if len(lista) > 1:
      meio = len(lista) // 2
      esquerda = lista[:meio]
      direita = lista[meio:]
      mergeSort(esquerda)
      mergeSort(direita)
      i = j = k = 0
      while i < len(esquerda) and j < len(direita):
          if esquerda[i]["pontuaçao"] > direita[j]["pontuaçao"]:
            lista[k] = esquerda[i]
            i += 1
          else:
              lista[k] = direita[j]
              j += 1
          k += 1
      while i < len(esquerda):
          lista[k] = esquerda[i]
          i += 1
          k += 1
      while j < len(direita):
          lista[k] = direita[j]
          j += 1
          k += 1

      while i < len(esquerda) and j < len(direita):
        if esquerda[i]["vitórias"] > direita[j]["vitórias"]:
          lista[k] = esquerda[i]
          i += 1
        else:
            lista[k] = direita[j]
            j += 1
        k += 1
      while i < len(esquerda):
        lista[k] = esquerda[i]
        i += 1
        k += 1
      while j < len(direita):
        lista[k] = direita[j]
        j += 1
        k += 1

      while i < len(esquerda) and j < len(direita):
        if esquerda[i]["saldo"] > direita[j]["saldo"]:
          lista[k] = esquerda[i]
          i += 1
        else:
            lista[k] = direita[j]
            j += 1
        k += 1
      while i < len(esquerda):
        lista[k] = esquerda[i]
        i += 1
        k += 1
      while j < len(direita):
        lista[k] = direita[j]
        j += 1
        k += 1


def selectionSort(lista, size):

  for ind in range(size):
      max_index = ind

      for j in range(ind + 1, size):
          # select the minimum element in every iteration
          if lista[j]["pontuaçao"] > lista[max_index]["pontuaçao"]:
            max_index = j
          elif lista[j]["pontuaçao"] == lista[max_index]["pontuaçao"] and lista[j]["vitórias"] > lista[max_index]["vitórias"]:
            max_index = j
          elif lista[j]["pontuaçao"] == lista[max_index]["pontuaçao"] and lista[j]["vitórias"] == lista[max_index]["vitórias"] and lista[j]["saldo"] > lista[max_index]["saldo"]:
            max_index = j
       # swapping the elements to sort the array
      (lista[ind], lista[max_index]) = (lista[max_index], lista[ind])

      
def insertionSort(lista):
    for i in range(1, len(lista)):
      chave = lista[i]
      j = i-1
      while j >= 0 and chave["pontuaçao"] > lista[j]["pontuaçao"]:
        lista[j + 1] = lista[j]
        j -= 1
      lista[j + 1] = chave

      while j >= 0 and chave["pontuaçao"] >= lista[j]["pontuaçao"] and chave["vitórias"] > lista[j]["vitórias"]:
        lista[j + 1] = lista[j]
        j -= 1
      lista[j + 1] = chave

      while j >= 0 and chave["pontuaçao"] >= lista[j]["pontuaçao"] and chave["vitórias"] >= lista[j]["vitórias"] and chave["saldo"] > lista[j]["saldo"]:
        lista[j + 1] = lista[j]
        j -= 1
      lista[j + 1] = chave


def partition(lista, low, high):
  pivot = lista[high]
  i = low - 1
  for j in range(low, high):
    if lista[j]["pontuaçao"] > pivot["pontuaçao"]:
      i = i + 1
      (lista[i], lista[j]) = (lista[j], lista[i])
    elif lista[j]["pontuaçao"] == pivot["pontuaçao"]:
      if lista[j]["vitórias"] > pivot["vitórias"]:
        i = i + 1
        (lista[i], lista[j]) = (lista[j], lista[i])
      elif lista[j]["vitórias"] == pivot["vitórias"]:
        if lista[j]["saldo"] > pivot["saldo"]:
          i = i + 1
          (lista[i], lista[j]) = (lista[j], lista[i])
  (lista[i + 1], lista[high]) = (lista[high], lista[i + 1])
  return i + 1

def quickSort(lista, low, high):
  if low < high:
    pi = partition(lista, low, high)
    quickSort(lista, low, pi - 1)
    quickSort(lista, pi + 1, high)

def bubbleSort(lista):
  n = len(lista)
  trocado = False

  for i in range(n-1):

      for j in range(0, n-i-1):
        if lista[j]["saldo"] < lista[j + 1]["saldo"]:
          trocado = True
          lista[j], lista[j + 1] = lista[j + 1], lista[j]
          
      for j in range(0, n-i-1):
        if lista[j]["vitórias"] < lista[j + 1]["vitórias"]:
          trocado = True
          lista[j], lista[j + 1] = lista[j + 1], lista[j]
          
      for j in range(0, n-i-1):
        if lista[j]["pontuaçao"] < lista[j + 1]["pontuaçao"]:
          trocado = True
          lista[j], lista[j + 1] = lista[j + 1], lista[j]
          
      if not trocado:
          return

tabela_brasileirao = [
  {"nome":"Palmeiras","pontuaçao":63,"vitórias":18, "saldo":26},
  {"nome":"Flamengo","pontuaçao":63,"vitórias":18, "saldo":17},
  {"nome":"Botafogo","pontuaçao":62,"vitórias":18, "saldo":23},
  {"nome":"Atlético-MG","pontuaçao":60,"vitórias":17, "saldo":19},
  {"nome":"Grêmio","pontuaçao":59,"vitórias":18, "saldo":4},
  {"nome":"Bragantino","pontuaçao":59,"vitórias":16, "saldo":15},
  {"nome":"Fluminense","pontuaçao":53,"vitórias":15, "saldo":3},
  {"nome":"Athlético-PR","pontuaçao":52,"vitórias":13, "saldo":8},
  {"nome":"Cuiabá","pontuaçao":48,"vitórias":13, "saldo":1},
  {"nome":"São Paulo","pontuaçao":47,"vitórias":12, "saldo":1},
  {"nome":"Internacional","pontuaçao":46,"vitórias":12, "saldo":-4},
  {"nome":"Fortaleza","pontuaçao":45,"vitórias":12, "saldo":-2},
  {"nome":"Cruzeiro","pontuaçao":44,"vitórias":11, "saldo":3},
  {"nome":"Corinthians","pontuaçao":44,"vitórias":10, "saldo":-4},
  {"nome":"Santos","pontuaçao":43,"vitórias":11, "saldo":-18},
  {"nome":"Vasco","pontuaçao":42,"vitórias":11, "saldo":-8},
  {"nome":"Bahia","pontuaçao":41,"vitórias":11, "saldo":-4},
  {"nome":"Goiás","pontuaçao":35,"vitórias":8, "saldo":-16},
  {"nome":"Coritiba","pontuaçao":29,"vitórias":8, "saldo":-29},
  {"nome":"América-MG","pontuaçao":21,"vitórias":4, "saldo":-35}  
]

shuffle(tabela_brasileirao)
for time in tabela_brasileirao:
  print(f"{time['nome']}:{time['pontuaçao']}\n")

print("--------------------------------------\n")
print("------------merge sort-----------------\n")
mergeSort(tabela_brasileirao) 


for time in tabela_brasileirao:
  print(f"{time['nome']}:{time['pontuaçao']}\n")

shuffle(tabela_brasileirao)
print("--------------------------------------\n")
print("-----------selection sort-------------\n")
selectionSort(tabela_brasileirao, len(tabela_brasileirao))

for time in tabela_brasileirao:
  print(f"{time['nome']}:{time['pontuaçao']}\n")

shuffle(tabela_brasileirao)
print("--------------------------------------\n")
print("-----------insertion sort-------------\n")
insertionSort(tabela_brasileirao)

for time in tabela_brasileirao:
  print(f"{time['nome']}:{time['pontuaçao']}\n")

shuffle(tabela_brasileirao)
print("--------------------------------------\n")
print("-----------quick sort-----------------\n")
quickSort(tabela_brasileirao, 0, len(tabela_brasileirao)-1)

for time in tabela_brasileirao:
  print(f"{time['nome']}:{time['pontuaçao']}\n")

shuffle(tabela_brasileirao)
print("--------------------------------------\n")
print("-----------bubble sort----------------\n")
bubbleSort(tabela_brasileirao)

for time in tabela_brasileirao:
  print(f"{time['nome']}:{time['pontuaçao']}\n")
