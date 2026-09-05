def processar_notas_arquivo(nomeArquivo):
    try:
        with open(nomeArquivo, "r", encoding="utf-8") as f:
         notas = f.read().split()
         for i  in range (0,len(notas)):
            notas[i] = float(notas[i])
            print(notas[i])

    except FileNotFoundError:
        print("ERRO, ARQUIVO NÃO ENCONTRADO")
    except ValueError:
        print("Um dos valores não é número")



if __name__ == '__main__':
    processar_notas_arquivo("notas.txt")