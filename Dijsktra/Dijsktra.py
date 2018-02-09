from grafo import Grafo
from math import inf

lista_vertices = []
dict_pesos = {}
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


def recebe_pesos(arestas):
    relacao_pesos_aresta = {}
    while True:
        try:
            pesos = [int(x) for x in input("Digite o peso de cada aresta: ").split(", ")]
            break
        except ValueError:
            print("Digite um valor numerico")

    for indice, aresta in enumerate(arestas):
        relacao_pesos_aresta[(arestas['a' + str(indice + 1)])] = pesos[indice]

    return relacao_pesos_aresta


def criar_vertices_index():
    """Guarda a relação de indices e vertices da matriz"""

    vertices_dict = {}
    for i in range(len(lista_vertices)):
        vertices_dict[i] = lista_vertices[i]

    return vertices_dict


def matriz_adjacencia(vertices_dict, peso_arestas):
    """Inicializa a matriz de adjacencia"""

    matriz = []
    for i in range(len(vertices_dict.keys())):
        matriz.append([])
        for j in range(len(vertices_dict.keys())):
            try:
                matriz[i].append(((lista_aresta.count((vertices_dict[i] + "-" + vertices_dict[j]))),
                                  peso_arestas[(vertices_dict[i] + "-" + vertices_dict[j])]))
            except KeyError:
                matriz[i].append(((lista_aresta.count((vertices_dict[i] + "-" + vertices_dict[j]))), 0))

    return matriz


def forma_tabular(matriz):
    """Imprime a matriz em formato tabular"""

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (j - 1) < len(matriz[i]):
                print("(" + str(matriz[i][j][0]) + ", " + str(matriz[i][j][1]) + ")", end=" ")
            else:
                print("(" + str(matriz[i][j][0]) + ", " + str(matriz[i][j][1]) + ")", end="")
        print("\n")


def criar_arestas_lista():
    """Cria uma lista so de arestas"""

    lista = []
    for i in dict_arestas.values():
        lista.append(i)
    return lista


def acha_caminho(caminho, index, inicial):
    if caminho[index] is None:
        return

    acha_caminho(caminho, caminho[index], inicial)

    print("%s " % lista_vertices[index], end=" ")


def imprime_caminho(caminho, indice_inicial, indice_final):
    print("\nDe %s até %s: " % (lista_vertices[indice_inicial], lista_vertices[indice_final]), end=" ")
    acha_caminho(caminho, indice_final, indice_inicial)


def menor_distancia(vertices):
    minimo = inf
    indice_minimo = None

    for i in range(len(vertices)):
        if vertices[i][1] is False and vertices[i][0] <= minimo:
            minimo = vertices[i][0]
            indice_minimo = i

    return indice_minimo


def dijsktra(matriz, vertices_indices, vertice_inicial, vertice_final):
    vertices = []
    caminho = [None] * len(vertices_indices.keys())
    indice_inicial = [int(indice) for indice, valor in vertices_indices.items() if valor == vertice_inicial][0]
    indice_final = [int(indice) for indice, valor in vertices_indices.items() if valor == vertice_final][0]

    for i in range(len(vertices_indices.keys())):
        vertices.append([inf, False])
    vertices[indice_inicial][0] = 0

    for i in range(len(vertices)):
        a = menor_distancia(vertices)

        vertices[a][1] = True

        for j in range(len(vertices)):
            if not vertices[j][1] and matriz[a][j][0] != 0 and vertices[a] != inf \
                    and vertices[a][0] + matriz[a][j][1] < vertices[j][0]:
                caminho[j] = a
                vertices[j][0] = vertices[a][0] + matriz[a][j][1]

    imprime_caminho(caminho, indice_inicial, indice_final)


def main():
    while True:
        vertice_inicial = input("Digite o vertice inicial: ").upper()
        vertice_final = input("Digite o vertice final: ").upper()
        if vertice_inicial not in lista_vertices or vertice_final not in lista_vertices:
            print("Digite um vertice valido")
        else:
            break
    dijsktra(matriz_adjacencia, vertices_index, vertice_inicial, vertice_final)


while True:
    try:
        lista_vertices = recebe_vertices()
        dict_arestas = recebe_arestas()
        lista_aresta = criar_arestas_lista()
        dict_pesos = recebe_pesos(dict_arestas)
        gr = Grafo(lista_vertices, dict_arestas)
        vertices_index = criar_vertices_index()
        matriz_adjacencia = matriz_adjacencia(vertices_index, dict_pesos)
        break
    except:
        print("Arestas ou vértices inválidos")

if __name__ == '__main__':
    main()

"""
testes
J, C, E, P, M, T, Z
a1(J-C), a2(E-C), a3(C-E), a4(C-P), a5(C-C), a6(C-M), a7(C-T), a8(M-T), a9(T-Z)
2, 3, 2, 4, 5, 6, 2, 9, 10
J, C, B
a1(J-C), a2(J-B), a3(C-B)
a1(J-C), a2(C-J), a3(C-B), a4(B-J)
a1(J-C), a2(J-B), a3(C-B), a4(J-J), a5(B-B), a6(C-C)
A, B, C
a1(A-B), a2(A-A), a3(B-A)
A, B, C, D, E
a1(A-B), a2(B-C), a3(C-A), a4(B-D), a5(D-E), a6(E-B)
"""
