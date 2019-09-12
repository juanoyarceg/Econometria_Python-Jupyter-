import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def descriptives_stats (dataframe):
    """
    Definición: La función  muestra las estadísticas descriptivas de un dataframe, dependiendo si es variable
    categórica, mostrará la frecuencia relativa, si es numérica, resumirá la media, la desviación standar,
    el rango y los cuartiles.
    Input: recibe un dataframe 
    Outpout: Imprime las estadísticas descriptivas numéricas o categóricas según corresponda
    """

    for i in dataframe:
        if len(dataframe[i].value_counts()) > 2:
            print(dataframe[i].describe(), "\n")
        else:
            print(dataframe[i].value_counts('%'), "\n")

def descriptives_plot(dataframe):
    """
    Descripción: Esta función recibe un data set y descrimina entre el tipo de variable para gráficar un histograma de frecuencias
    en el caso de ser una variable numérica (int 64) o devuelve un gráfico de barras con las frecuencias de las variables categóricas (Objetc: String)
    
    Input:DataFrame: dataframe de Pandas con las variables a analizar
    
    Outpout: Imprime como salidas los histogramas de frecuencia o los gráficos de barras de frecuencias
    """
    for i in dataframe.columns:
        if dataframe[i].dtype == 'O':


            dataframe[i].value_counts().plot(kind='bar',title='Frecuencias de: '+i)
            plt.xlabel("")
            plt.rcParams["figure.figsize"] = (6, 6) 
            plt.tight_layout()
            plt.show()
            print('\n')    
        else:
            plt.hist(dataframe[i], alpha=1, color='gray', label=i, normed=True)
            plt.axvline(dataframe[i].mean(), lw=3, color='tomato', label='Media')
            plt.axvline(dataframe[i].median(), lw=3, color='green', label='Mediana')
            plt.title('Histograma: '+ i)
            plt.legend()
            plt.show()
            print('\n')

def corr_means(dataframe, significative=0.5):
    """
    Definición: Función que extrae las correlaciones significativas a un nivel asignado
    
    Input: dataframe a correlacionar, significative (float) de 0 hasta 1.0 que indica el nivel de significancia a filtrar, por 
    defecto viene asignado con un valor superior o igual a 0.5 
    
    Outpout:Imprime las correlaciones positivas y negativas significativas
    """


    names=dataframe.corr().columns.tolist()

    for element in names:
        corr=dataframe.corr()[element].sort_values(ascending=False)
        means_values_positives= pd.Series(corr).where(lambda x  : x>=significative).dropna() 
        means_values_negatives= pd.Series(corr).where(lambda x  : x<=-significative).dropna()


        print("Correlaciones significativas positivas: ",means_values_positives,"\n","\n","Correlaciones significativas negativas: ","\n",means_values_negatives,"\n" )
        
        

            


def null_lost (dataframe, var, print_list=False):
    """
    Definición: La función  analiza la cantidad de casos perdidos de una serie en el dataframe
    Input: recibe un dataframe, un string con el nombre de la variable del dataframe y un parametro 
    para imprimir la lista de páíses, en caso de que se disponga de esa variable (False=default)
    Outpout: Imprime la variable, la cantidad de casos perdiso y el porcentaje de la muestra
    """
    tmp = dataframe
    tmp['flagnull'] = tmp[var].isnull()
    count_na = 0

    for i, r in tmp.iterrows():
        if r['flagnull'] is True:
            count_na += 1
            if print_list is True:
                print( r['cname'])

    if print_list is True:
        print("Países sin registros de {0}\n".format(var))
    print("Casos perdidos para {0}:\nCantidad de Casos: {1}\nPorcentaje de la muestra {2}\n".format(var, count_na, count_na/len(tmp)))

