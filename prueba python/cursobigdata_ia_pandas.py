#LIBRERIA PARA ANALISIS DE DATOS / ESTRUCTURA DE DATOS Y OPERACIONES PARA MANIPULAR DATOS
import pandas as pd

archivo_csv = 'https://curso-big-data-e-ia.s3.eu-west-1.amazonaws.com/TopSellingAlbums.csv'

df = pd.read_csv(archivo_csv) #DESCARGAMOS EL ARCHIVO Y LO CARGAMOS EN UN DATAFRAME LLAMADO DF
df
df.head()
df.head(2)

archivo_xlsx = 'https://curso-big-data-e-ia.s3.eu-west-1.amazonaws.com/TopSellingAlbums.xlsx'
df_xlsx = pd.read_excel(archivo_xlsx)
df_xlsx.head()
df_xlsx.head(2)

duracion = df_xlsx[['Length']] # Extraemos la columna como un dataframe
duracion
type(duracion)

duracion = df_xlsx['Length'] # Extraemos la columna como una serie
type(duracion)

duracion


columnas = df[['Artist','Length','Genre']]
print(columnas)

df.iloc[1,1] #iloc - item location
df.loc[1,'Album']
df.iloc[0:2,0:3]

df.size

