from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np
import streamlit as st
import seaborn as sns
from PIL import Image
import utilidades as util
import sklearn as skl

#configuramos los encabezados de página
st.set_page_config(page_title='Informe de la Liga Betplay 2024-2',
                    page_icon='📊', # Puedo obtener los íconos de https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
                    layout='centered', 
                    initial_sidebar_state='expanded'
                    )

# Llamamos a la función generarMenu
util.generarMenu()

# Cargo el Dat Frame
ruta = 'Data\\tctclean.csv'
df = pd.read_csv(ruta)

# Estructura de presentación
util.genVisualPagina('Datos de la Liga Betplay 2024-2', 
                     0.5, 5, 0.5, 
                     'center', 
                     'Cantidad de goles marcados por cada equipo', 
                     df)
