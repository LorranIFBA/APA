import produto


def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        mergeSort(esquerda)
        mergeSort(direita)
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i].nome <= direita[j].nome:
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

def buscaBin(lista, esquerda, direita, nome):
    while esquerda <= direita:
        meio = esquerda +(direita - esquerda) // 2

        if lista[meio].nome == nome:
            return meio
        elif lista[meio].nome < nome:
            esquerda = meio + 1
        else:
            direita = meio -1
    return -1


class Estoque:
    def __init__(self, produtos):
        self.produtos = produtos

    def adicionar(self, nome_produto, id_produto):
        novo_produto = produto.Produto(nome=nome_produto, id=id_produto)
        self.produtos.append(novo_produto)

    def remover(self, id_produto):
        for item in self.produtos:
            if item.id == id_produto:
                self.produtos.remove(item)
                break

    def busca(self, nome):
        if len(self.produtos) < 150:
          idx = buscaBin(self.produtos, 0, len(self.produtos)-1 , nome)
        else:
          idx = buscaBin(self.produtos, 0, 150, nome)
          if idx == -1:
            idx = buscaBin(self.produtos, 151, len(self.produtos)-1 , nome)
          
        if idx != -1:
          return self.produtos[idx].id
        else:
          return -1
      
    def ordenar(self):
        mergeSort(self.produtos)
