def apresentacao_dos_dados(dataframe):

    #Convertendo os dados (string) para dados (float) e ajustando sua precisão
    dataframe['Estadual'] = dataframe['Estadual'].astype(float) / 10000
    dataframe['Nacional'] = dataframe['Nacional'].astype(float) / 10000

    return dataframe