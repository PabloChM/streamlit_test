import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import utilidades as util
from PIL import Image


# Corremos streamlit run app.py en la terminal
# para abrir la interfaz

# Página de presentación o index, esta debe ser la primer instrucción del st que se ejecute
st.set_page_config(page_title='Liga Betplay 2024-2',
                    page_icon='🏆', # Puedo obtener los íconos de https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
                   layout='wide', 
                   initial_sidebar_state='expanded'
                   )
                   
# Llamamos a la función generarMenu
util.generarMenu ()

# Estructura de presentación
left_col, center_col, right_col = st.columns([1, 4, 1], 
                                             vertical_alignment='center'
                                             )
# Edito la columna central
with center_col:
    st.title('Informe de la liga Betplay 2024-2')
    st.write("""
En este espacio se presentará un informe de la liga Betplay 2024-2, 
en el cual se mostrarán los resultados de los partidos, la tabla de 
posiciones, el desempeño por equipo y el análisis estadístico\n
En la página informes se podrán ver los datos y su análisis         
             """)
    imagen2 = Image.open(r'Media\fcf.png')
    st.image(imagen2, 
             use_container_width=True, 
             width=500, 
             caption='Federación Colombiana de Fútbol'
             )

#Edito la columna izquierda
with left_col:
    st.write('')