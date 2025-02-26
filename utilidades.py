import pandas as pd
import streamlit as st
from PIL import Image
from matplotlib import pyplot as plt
import seaborn as sns

# Defino una función para generar el menú lateral
def generarMenu():
    # Agregamos un menú lateral
    with st.sidebar:
        # Creamos las dos columnas que tiebne la barra lateral
        col1,col2 = st.columns(2)
        # Doy formato a la primera columna
        with col1:
            #Cargo una imagen a la primera columna
            imagen = Image.open('Media\logo_dimayor.png')
            st.image(imagen, use_container_width=False, width=120)
        # Doy formato a la segunda columna
        with col2:
            st.header('Liga BetPlay 2024-2') 
        st.page_link('app.py',
                 label='Home',
                 icon='🏠'
                 )
        st.page_link('Pages\informe.py',
                    label='Informe',
                    icon='📊'
                    )

def genVisualPagina (titulo, sizeCol1, sizeCol2, sizeCol3, vAlineacion, tCol,df):
    #Cargo el Data Frame
    df2 = pd.DataFrame(df)

    # Título de la página
    st.title(titulo)

    # Estructura de presentación
    col1, col2, col3 = st.columns([sizeCol1, sizeCol2, sizeCol3], vertical_alignment=vAlineacion)
    
    with col2:
        # Título de la columna central
        st.markdown(tCol)
        # Hago que el index del Data Frame sea la columna Local
        df2.set_index('Local', inplace=True)
        # Imprimo el Data Frame
        st.write(df2, unsafe_allow_html=False)
        # Nombro el tipo de gráfico que voy a generar
        st.markdown("Gráfico de barras")
        # Genero las medidas del gráfico
        sns.set_theme(rc={'figure.figsize':(8,8)})
        sns.set_style('whitegrid')
        # Genero el DF de goles
        total = df2.groupby('Local')[['Goles Local','Goles Visitante']].sum()
        goles = pd.DataFrame(total)
        goles['Goles Totales'] = goles['Goles Local'] + goles['Goles Visitante']
        goles = goles.sort_values(by='Goles Totales', ascending=False)
        goles =  goles.reset_index()
        resultados = goles.groupby(['Local']).sum()
        resultados.plot(kind='bar', 
                        stacked=True, 
                        figsize=(10,12))
        plt.tight_layout()
        st.pyplot(plt)
            
            