import estoque
import produto

loop = True
lista_estoque = []
estoque_ = estoque.Estoque(lista_estoque)

with open("estoque.txt", "r") as arq:
    for line in arq:
        if line == "":
            break
        splitline = line.split(":")
        estoque_.adicionar(nome_produto=splitline[0], id_produto=int(splitline[1].strip()))


while loop:
    if input("Deseja adicionar algum produto? (s/n)") == "s":
        nome_produto = input("Digite o nome do produto: ")
        id_produto = int(input("Digite o id do produto: "))
        estoque_.adicionar(nome_produto=nome_produto, id_produto=id_produto)
    else:
        loop = False


#estoque_.ordenar()

codigo = estoque_.busca("sal")
if codigo != -1:
    print(f"O codigo do produto pesquisado e: {codigo}")
else:
    print("Produto nao encontrado")

with open("estoque.txt", "w") as arq:
    for item in estoque_.produtos:
        arq.write(f"{item.nome}:{item.id}\n")



