from random import shuffle

#Algoritmo de ordenaçao

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
      
#Lista ordenada

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
# Randomização da lista para testar o código de ordenação
shuffle(tabela_brasileirao)
for time in tabela_brasileirao:
  print(f"{time['nome']}:{time['pontuaçao']}\n")

print("--------------------------------------\n")

mergeSort(tabela_brasileirao) #Chamada de ordenaçao
for time in tabela_brasileirao:
  print(f"{time['nome']}:{time['pontuaçao']}\n")



def retornaPosicao(lista, nome, posicao=0): #primeira funçao
  if lista[posicao]["nome"] == nome:
    return posicao
  else:
    return retornaPosicao(lista, nome, posicao+1)

def exibePrimeiros(lista, posicao=0): #segundo e quarto pontos
  if posicao < 5:
    print(f"{lista[posicao]['nome']}:{lista[posicao]['pontuaçao']} - Diferença de pontuação com {lista[posicao+1]['nome']}:{lista[posicao]['pontuaçao'] - lista[posicao+1]['pontuaçao']}")
    exibePrimeiros(lista, posicao+1)

def exibeUltimos(lista, posicao=0): #terceiro e quinto pontos
  cutoff = len(lista)-6
  if posicao == len(lista):
    return

  if posicao > cutoff:
    if posicao < len(lista)-1:
      print(f"{lista[posicao]['nome']}:{lista[posicao]['pontuaçao']} - Diferença de pontuação com {lista[posicao+1]['nome']}:{lista[posicao]['pontuaçao'] - lista[posicao+1]['pontuaçao']}")
    else:
      print(f"{lista[posicao]['nome']}:{lista[posicao]['pontuaçao']} - Último colocado")
    exibeUltimos(lista, posicao+1)
  else:
    exibeUltimos(lista, posicao+1)


def exibeMetade(lista, posicao=0):  #sexto ponto
  if posicao == len(lista)/2:
    return
  print(f"{lista[posicao]['nome']}:{lista[posicao]['pontuaçao']} - Diferença de pontuação com {lista[posicao+1]['nome']}:{lista[posicao]['pontuaçao'] - lista[posicao+1]['pontuaçao']}")
  exibeMetade(lista, posicao+1)
  


# RESULTADOS

print(f"O time Cuiabá está na posicao {retornaPosicao(tabela_brasileirao, 'Cuiabá')+1} do brasileirao\n")

exibePrimeiros(tabela_brasileirao)
print("\n")
exibeUltimos(tabela_brasileirao)
print("\n")
exibeMetade(tabela_brasileirao)
