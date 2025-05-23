#def soma(valor1:float, valor2:float) -> float:
 #   resultado = valor1 + valor2
  #  return resultado

#valor3 = float(input("insira um valor:"))
#valor4 = float(input("insira um valor: "))

#valor5 = soma(valor1=valor3 ,valor2=valor4)



#print(valor5)

#########
#########
import csv
path_arquivo = "vendas.csv"

def ler_csv(nome_arquivo_csv:str) ->list[dict]:
    """
    funçao que le um arquivo csv e retorna uma lista
    de dicionarios
    """

    lista = []
    with open(nome_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)