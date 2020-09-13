'''
XIII Maratona Santo Scuderi de Programação

Problema F - Pandemia

Autor: Lucas Anjos | github: https://www.github.com/luskas8
'''

# Inicio:
def main():
    nLinha, nColunas = [int (x) for x in input().split()]

    # quadro com valores das resistências de cada pessoa
    quadro = []

    for i in range(nLinha):
            # Pegando dados de resistência de casa pessoa
            quadro.append([int(j) for j in input().split()])
    #end for i

    lInfectado, cInfectado, illnessPower = [int(x) for x in input().split()]

    # Inicialização das matrizes de infectados e pessoas analizadas como falso
    infectados = [[False for i in range(nColunas)] for j in range(nLinha)]
    passed = [[False for i in range(nColunas)] for j in range(nLinha)]

    # Matriz de infectados
    infectar(nLinha, nColunas, infectados, quadro, passed, lInfectado, cInfectado, illnessPower)

    infectadosTotal = 0

    for infectado in infectados:
        for i in infectado:
            if (i): infectadosTotal += 1

    print(infectadosTotal)
# Fim main

# Verifica se está dentro do limite de linhas do quadro
def dentroLinhas(linhas, currentL): return (currentL < linhas and currentL >= 0)

# Verifica se está dentro do limite de colunas do quadro
def dentroColunas(coluna, currentC):return (currentC < coluna and currentC >= 0)

# Função para infectar todos em volta
'''
    Esta função infecta a pessoa de posição: [currentL][currentC] => [linha][coluna], armazenando
    o estado de infectada ou não numa 2° matriz chamada na main por infectados. E altera o estado
    da pessoa de True ou False para os casos de ja analizada ou não.
'''
def infectar(l, c, infectados: list, quadro: list, passed: list, currentL, currentC, power):
    # Verifica se existe dentro da matriz
    if (dentroLinhas(l, currentL) and dentroColunas(c, currentC)):
        # Pergunta se já passaram ou não por está pessoa
        if not passed[currentL][currentC]:
            # Pergunta se o vírus é ou não maior que a resitência da pessoa
            if (quadro[currentL][currentC] < power):
                # Se sim infecta-a
                infectados[currentL][currentC], passed[currentL][currentC] = True, True
                # Se não retorna e para a execução desta função sobre esta dada pessoa
            else: return

            '''
                Caso a pessoa seja infectada ela irá infectar todos a sua volta entrando nesse:
            '''
            # Infectando o de baixo
            if (dentroLinhas(l, currentL + 1)):
                if not infectados[currentL + 1][currentC]:
                    if (quadro[currentL + 1][currentC] < power):
                        infectar(l, c, infectados, quadro, passed, currentL + 1, currentC, power)
                    # End if 3
                # End if 2
                else: infectar(l, c, infectados, quadro, passed, currentL + 1, currentC, power)
            # End if 1

            # Infectando o de cima
            if (dentroLinhas(l, currentL - 1)):
                if not infectados[currentL - 1][currentC]:
                    if (quadro[currentL - 1][currentC] < power):
                        infectar(l, c, infectados, quadro, passed, currentL - 1, currentC, power)
                    # End if 3
                # End if 2
                else: infectar(l, c, infectados, quadro, passed, currentL - 1, currentC, power)
            # End if 1

            # Infectando o da direita
            if (dentroColunas(c, currentC + 1)):
                if not infectados[currentL][currentC - 1]:
                    if (quadro[currentL][currentC + 1] < power):
                        infectar(l, c, infectados, quadro, passed, currentL, currentC + 1, power)
                    # End if 3
                # End if 2
                else: infectar(l, c, infectados, quadro, passed, currentL, currentC + 1, power)
            # End if 1

            # Infectando o da esquerda
            if (dentroColunas(c, currentC - 1)):
                if not infectados[currentL][currentC - 1]:
                    if (quadro[currentL][currentC - 1] < power):
                        infectar(l, c, infectados, quadro, passed, currentL, currentC - 1, power)
                    # End if 3
                # End if 2
                else: infectar(l, c, infectados, quadro, passed, currentL, currentC - 1, power)
            # End if 1
    #Retorno para caso ele já foi passado ou não esteja dentro da matriz
    return
# Fim infectar

if __name__ == '__main__':
    main()
