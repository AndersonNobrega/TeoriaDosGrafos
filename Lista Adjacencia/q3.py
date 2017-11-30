from grafo import Grafo

lista_vertices = []
dict_arestas = {}
lista_adjacencia = {}


def recebe_vertices():
    vertices = input("Digite todos os vértices: ").split(", ")
    return vertices


def recebe_arestas():
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


def vertice_adjacente():
    for i in lista_vertices:
        if i + "-" + i in dict_arestas.values():
            return True
    return False


def vertices_nao_adjacente():
    lista_nao_adjacantes = []
    for i in lista_vertices:
        for j in lista_vertices:
            if i + "-" + j not in dict_arestas.values() and j + "-" + i not in dict_arestas.values():
                if j + "-" + i not in lista_nao_adjacantes:
                    lista_nao_adjacantes.append((i + "-" + j))

    return lista_nao_adjacantes


def aresta_paralelas():
    cont = 0
    for i in lista_vertices:
        for j in lista_vertices:
            cont += lista_aresta.count((i + "-" + j))
            cont += lista_aresta.count((j + "-" + i))
            if cont >= 2:
                return True
            else:
                cont = 0
    return False


def arestas_incidem(vertice):
    lista = []
    for i in dict_arestas.keys():
        if vertice in dict_arestas[i]:
            lista.append(i)
    return lista


def grau_vertice(vertice):
    cont = 0
    for i in lista_vertices:
        if vertice + "-" + i in lista_aresta:
            cont += 1
        if i + "-" + vertice in lista_aresta and i != vertice:
            cont += 1
    return cont


def eh_completo():
    lista = vertices_nao_adjacente()

    if len(lista) == 0:
        return True
    else:
        for i in lista_vertices:
            for j in lista_vertices:
                if i + "-" + j in lista and j != i:
                    return False
        return True


def criar_arestas_lista():
    lista = []
    for i in dict_arestas.values():
        lista.append(i)
    return lista


def cria_lista_adjacencia():
    lista_adjacencia = {}
    for vertice in lista_vertices:
        lista_adjacencia[vertice] = set()
        for arestas in lista_aresta:
            if arestas[0] == vertice:
                lista_adjacencia[vertice].add(arestas[2])
            if arestas[2] == vertice:
                lista_adjacencia[vertice].add(arestas[0])

    return lista_adjacencia


def encontra_comprimento(grafo, inicio, objetivo):
    pilha = [(inicio, [inicio])]
    while pilha:
        (vertice, caminho) = pilha.pop()
        for proximo in grafo[vertice] - set(caminho):
            if proximo == objetivo:
                yield caminho + [proximo]
            else:
                pilha.append((proximo, caminho + [proximo]))


def maior_comprimento():
    maior_caminho = 0
    for i in lista_vertices:
        for j in lista_vertices:
            if i != j:
                for caminho in list(encontra_comprimento(lista_adjacencia, i, j)):
                    if len(caminho) - 1 > maior_caminho:
                        maior_caminho = len(caminho) - 1
    return maior_caminho


def main():
    # Copiei o menu msm pq sou preguicoso
    while True:
        print("\na - Encontre todos os pares de vértices não adjacentes.\n"
              "b - Há algum vértice adjacente a ele mesmo?\n"
              "c - Há arestas paralelas?\n"
              "d - Saber o grau de um vertice qualquer.\n"
              "e - Saber as arestas incidentes de um vertice\n"
              "f - Esse grafo é completo?\n"
              "g - Maior caminho nesse grafo.\n"
              "h - Sair do programa.\n")
        escolha = input("Informe uma opção: ").lower()
        if escolha == 'a':
            print(vertices_nao_adjacente())
        elif escolha == 'b':
            print(vertice_adjacente())
        elif escolha == 'c':
            print("Aresta paralelas: " + str(aresta_paralelas()))
        elif escolha == 'd':
            vertice = input("Qual vertice: ")
            print("Grau do vértice: %d" % grau_vertice(vertice))
        elif escolha == 'e':
            vertice = input("Qual vertice: ")
            print("Arestas que incidem: " + str(arestas_incidem(vertice)))
        elif escolha == 'f':
            print(eh_completo())
        elif escolha == 'g':
            print(maior_comprimento())
        elif escolha == 'h':
            return


while True:
    try:
        lista_vertices = recebe_vertices()
        dict_arestas = recebe_arestas()
        gr = Grafo(lista_vertices, dict_arestas)
        lista_aresta = criar_arestas_lista()
        lista_adjacencia = cria_lista_adjacencia()
        break
    except:
        print("Arestas ou vértices inválidos")

if __name__ == '__main__':
    main()

# testes
# J, C, E, P, M, T, Z
# a1(J-C), a2(E-C), a3(C-E), a4(C-P), a5(C-C), a6(C-M), a7(C-T), a8(M-T), a9(T-Z)
# J, C, B
# a1(J-C), a2(J-B), a3(C-B)
# a1(J-C), a2(J-B), a3(C-B), a4(J-J), a5(B-B), a6(C-C)
# A, B, C
# a1(A-B), a2(A-A), a3(B-A)
