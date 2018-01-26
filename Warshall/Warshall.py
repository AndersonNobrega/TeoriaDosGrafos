from grafo import Grafo
from copy import deepcopy

lista_vertices = []
dict_arestas = {}
vertices_index = {}


def recebe_vertices():
    """Recebe os vertices do usuario"""

    vertices = input("Digite todos os vértices: ").split(", ")
    return vertices


def recebe_arestas():
    """Recebe as arestas do usuario: a1(A-B)"""

    arestas_dict = {}
    while True:
        arestas = input("Digite as arestas: ").split(", ")
        condicao = True
        for i in range(len(arestas)):
            temp = ""
            for j in range(len(arestas[i])):
                if ")" not in arestas[i] or "(" not in arestas[i] or "-" not in arestas[i] or arestas[i][0] == "(":
                    condicao = False
                    break
                elif arestas[i][j] == "(":
                    if arestas[i][j + 3].isalpha():
                        arestas_dict[temp] = arestas[i][j + 1:len(arestas[i][j]) - 2]
                    else:
                        condicao = False
                    break
                elif arestas[i][j] == ")":
                    condicao = False
                    break
                temp += arestas[i][j]

        if not condicao:
            print("Arestas inválidos")
        else:
            return arestas_dict


def criar_vertices_index():
    """Guarda a relação de indices e vertices da matriz"""

    vertices_dict = {}
    for i in range(len(lista_vertices)):
        vertices_dict[i] = lista_vertices[i]

    return vertices_dict


def criar_arestas_lista():
    """Cria uma lista so de arestas"""

    lista = []
    for i in dict_arestas.values():
        lista.append(i)
    return lista


def matriz_adjacencia(vertices_dict):
    """Inicializa a matriz de adjacencia"""

    matriz = []
    for i in range(len(vertices_dict.keys())):
        matriz.append([])
        for j in range(len(vertices_dict.keys())):
            matriz[i].append(lista_aresta.count((vertices_dict[i] + "-" + vertices_dict[j])))

    return matriz


def forma_tabular(matriz):
    """Imprime a matriz em formato tabular"""

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (j - 1) < len(matriz[i]):
                print(matriz[i][j], end=" ")
            else:
                print(matriz[i][j], end="")
        print("\n")


def maior(num1, num2):
    if num1 != 0 or num2 != 0:
        return 1
    else:
        return 0


def warshall(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[coluna][linha] > 0:
                for k in range(len(matriz)):
                    matriz[coluna][k] = maior(matriz[coluna][k], matriz[linha][k])

    return matriz


def main():
    matriz_caminhos = warshall(deepcopy(matriz_adjacencia))
    forma_tabular(matriz_caminhos)


while True:
    try:
        lista_vertices = recebe_vertices()
        dict_arestas = recebe_arestas()
        gr = Grafo(lista_vertices, dict_arestas)
        lista_aresta = criar_arestas_lista()
        vertices_index = criar_vertices_index()
        matriz_adjacencia = matriz_adjacencia(vertices_index)
        break
    except:
        print("Arestas ou vértices inválidos")

if __name__ == '__main__':
    main()
