import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Leer los datos del archivo CSV
df = pd.read_csv("Dataset/Customer-Churn-Records.csv")


"""
# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)
"""



# --- Tu gráfica ---
fig = plt.figure(figsize=(4,5))
ax = sns.countplot(
    data=df,
    x="Churn",
    palette=['#bee7e8', '#bf4342'],
    edgecolor="black",
    hue="Churn"
)

plt.title("Churn counts")

for container in ax.containers:
    ax.bar_label(container)

# --- Mostrar en Streamlit ---
st.pyplot(fig)

