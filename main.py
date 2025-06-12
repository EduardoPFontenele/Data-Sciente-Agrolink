import pandas as pd

from formatacao import apresentacao_dos_dados
from tipagem_dados import caracterização_inicial
from medidas_de_locacao import centralidadeEN, DispersaoEN, AssociacaoEN

def main():

    #Local onde se encontra os dados
    url ="https://www.agrolink.com.br/cotacoes/historico/mt/soja-em-grao-sc-60kg"

    #Lendo os dados do url com pandas
    tabela = pd.read_html(url)[0]

    tabela_formatada = apresentacao_dos_dados(tabela)
    tipo_variaveis = caracterização_inicial(tabela_formatada)

    #Menu iterativo para verificar as informações
    while True:
        print(f"\n<========== AGROLINK ==========>\n")
        print(f"1. Caracterização Inicial dos tipos dos Atributos.")
        print(f"2. Verificar Centralidade.")
        print(f"3. Verificar Dispersão.")
        print(f"4. Verificar Associação.")
        print(f"5. Sair")

        try:
            opcao = int(input("\nInforme a operação que deseja realizar: "))

            if opcao == 1:
                print(f"\n<<===== TIPAGEM DOS DADOS =====>\n")
                print(tipo_variaveis)

                print(f"\n'Mês / Ano' : Temporal.")
                print(f"'Estadual': Quantitativa contínua.")
                print(f"'Nacional': Quantitativa contínua.'")
                print(f"_"*30)

            
            elif opcao == 2:
                print(f"\n<===== CENTRALIDADE =====>\n")
                centralidadeEN(tabela_formatada)
                print(f"_"*30)

            elif opcao == 3:
                print(f"\n<===== DISPERSÃO =====>\n")
                DispersaoEN(tabela_formatada)
                print(f"_"*30)

            elif opcao == 4:
                print(f"\n<===== ASSOCIAÇÃO =====>\n")
                AssociacaoEN(tabela_formatada)
                print(f"_"*30)

            elif opcao == 5:
                print(f"\nEncerrando Programa . . .")
                break

            else:
                print(f"\nOpção Inválida! Escolha uma opção de 1 à 5.")

        except ValueError :
            print(f"\nInforme um valor inteiro para realizar as operações!")


if __name__ == "__main__":
    main()