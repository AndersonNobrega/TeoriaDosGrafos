from grafo import Grafo

def recebe_vertices():
    vertices = input("Digite todos os vértices: ").split(", ")
    return vertices

def recebe_arestas():
    arestas_dict = {}
    while True:
        arestas = input("Digite as arestas: ").split(",")
        condicao = True
        for i in range(len(arestas)):
            temp = ""
            for j in range(len(arestas[i])):
                if ")" not in arestas[i] or "(" not in arestas[i] or "-" not in arestas[i] or arestas[i][0] == "(":
                    condicao = False
                    break
                elif arestas[i][j] == "(":
                    if arestas[i][j+3].isalpha():
                        arestas_dict[temp] = arestas[i][j+1:len(arestas[i][j])-2]
                    else:
                        condicao = False
                    break
                elif arestas[i][j] == ")":
                    condicao = False
                    break
                temp += arestas[i][j]
        
        if condicao == False:
            print("Arestas inválidos")
        else:
            return arestas_dict

while True:
    try:
        gr = Grafo(recebe_vertices(), recebe_arestas())
        break
    except:
        print("Arestas ou vértices inválidos")

print(gr)