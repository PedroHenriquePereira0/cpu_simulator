memoria = [0] * 64
R0 = 0
R1 = 0
R2 = 0
PC = 0
instrucoes = []

def carregar_programa(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.split('#')[0].strip()
            if linha:
                instrucoes.append(linha)

def executar(instrucao):
    global R0, R1, R2, PC, memoria

    partes = instrucao.split()
    comando = partes[0]

    if comando == "LOAD":
        reg = partes[1].replace(",", "")
        valor = partes[2]

        if valor.startswith("[") and valor.endswith("]"):
            endereco = int(valor[1:-1])
            if reg == "R0":
                R0 = memoria[endereco]
            elif reg == "R1":
                R1 = memoria[endereco]
            elif reg == "R2":
                R2 = memoria[endereco]
        else:
            if reg == "R0":
                R0 = int(valor)
            elif reg == "R1":
                R1 = int(valor)
            elif reg == "R2":
                R2 = int(valor)

    elif comando == "STORE":
        endereco = int(partes[1][1:-2])
        reg = partes[2]
        if reg == "R0":
            memoria[endereco] = R0
        elif reg == "R1":
            memoria[endereco] = R1
        elif reg == "R2":
            memoria[endereco] = R2

    elif comando == "ADD":
        reg1 = partes[1].replace(",", "")
        reg2 = partes[2]

        if reg1 == "R0":
            if reg2 == "R0": R0 += R0
            if reg2 == "R1": R0 += R1
            if reg2 == "R2": R0 += R2
        elif reg1 == "R1":
            if reg2 == "R0": R1 += R0
            if reg2 == "R1": R1 += R1
            if reg2 == "R2": R1 += R2
        elif reg1 == "R2":
            if reg2 == "R0": R2 += R0
            if reg2 == "R1": R2 += R1
            if reg2 == "R2": R2 += R2

    elif comando == "HLT":
        return False

    return True

def executar_cpu():
    global PC
    continuar = True
    while continuar and PC < len(instrucoes):
        instrucao = instrucoes[PC]
        print(f"\nExecutando (linha {PC}): {instrucao}")
        continuar = executar(instrucao)
        if continuar:
            PC += 1
        mostrar_estado()

def mostrar_estado():
    print(f"R0 = {R0}, R1 = {R1}, R2 = {R2}, PC = {PC}")
    print(f"Memória[30] = {memoria[30]}")
    print("-" * 30)

if __name__ == "__main__":
    nome = input("Nome do arquivo do programa (ex: exemplo.txt): ")
    carregar_programa(nome)
    executar_cpu()
