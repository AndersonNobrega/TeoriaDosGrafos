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
            matriz[i].append(lista_aresta.count((vertices_dict[i] + "-" + vertices_dict[j])) +
                             lista_aresta.count((vertices_dict[j] + "-" + vertices_dict[i])))

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


def caminho_euleriano(matriz):
    """Descobre se o grafo possui caminho euleriano"""

    if eh_conexo(matriz) is False:
        print("Não existe caminho eureliano")
    else:
        total = 0
        i = 0
        while (total <= 2) and (i < len(matriz)):
            grau = 0
            for j in range(len(matriz)):
                grau += matriz[i][j]
                grau += matriz[j][i]
            if grau % 2 == 1:
                total += 1
            i += 1
        if total > 2:
            print("Não existe caminho eureliano")
        else:
            print("Existe caminho eureliano")


def eh_conexo(matriz):
    """Descobre se o grafo é conexo"""

    for inicio in lista_vertices:
        pilha = [[inicio]]
        visitados = []

        while pilha:
            caminhos = pilha.pop(0)
            for i in caminhos:
                if i not in visitados:
                    visitados.append(i)
            indice_vertice = lista_vertices.index(caminhos[-1])
            for indice, vertice in enumerate(lista_vertices):
                if matriz[indice_vertice][indice] != 0 and vertice not in caminhos:
                    pilha.append(caminhos + [vertice])

        if len(visitados) != len(lista_vertices):
            return False
    return True


def main():
    caminho_euleriano(matriz_adjacencia)


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
