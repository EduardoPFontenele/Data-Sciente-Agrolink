def centralidadeEN(dataframe):

    #Calcule a Media
    Media = dataframe[['Estadual','Nacional']].mean()

    #Mostra a Moda
    Moda = dataframe[['Estadual','Nacional']].mode()

    #Calcula a Mediana
    Mediana = dataframe[['Estadual','Nacional']].median()

    #Mostrando os valores
    print(f"\nMedia (Estadual e Nacional) =\n{Media}")
    print(f"\nModa (Estadual e Nacional) =\n{Moda}\n(Não possui moda)")
    print(f"\nMediana (Estadual e Nacional) =\n{Mediana} ")

def DispersaoEN(dataframe):

    #Calcula o nivel de dispersão da média aritmética
    Desvio_medio = dataframe[['Estadual','Nacional']].std()

    #Calcula o nivel de dispersão dos dados em relação à media
    Variancia = dataframe[['Estadual','Nacional']].var()

    #Calcula a amplitude
    Amplitude = (dataframe[['Estadual', 'Nacional']].max()) - (dataframe[['Estadual','Nacional']].min())     

    #Mostrando os valores
    print(f"\nDesvio Medio (Estadual e Nacioanl) = \n{Desvio_medio}")
    print(f"\nVariancia (Estadual e Nacional) = \n{Variancia}")
    print(f"\nAmplitude (Estadual e Nacional) = \n{Amplitude}")


def AssociacaoEN(dataframe):

    #Calcula a direção de relacionamento entre duas variáveis
    Covariancia = dataframe[['Estadual','Nacional']].cov()

    #Calcula a força e direcão do relacionamento linear entre duas variáveis
    Correlacao = dataframe[['Estadual','Nacional']].corr()

    #Mostrando os valores
    print(f"\nCovariância (Estadual e Nacional) = \n{Covariancia}")
    print(f"\nCoeficiente de Correlação de Pearson (Estadual e Nacional) = \n{Correlacao}")