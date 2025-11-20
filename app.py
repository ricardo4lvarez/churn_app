import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Leer los datos del archivo CSV
df = pd.read_csv("Database/Customer-Churn-Records.csv")


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
#%% Limpieza EDA
df.drop(columns=["RowNumber", "CustomerId", "Surname"], axis=1, inplace=True)
df.rename(columns={"Exited":"Churn"}, inplace=True)
variables_cat = ["Tenure", "Geography", "Gender", "NumOfProducts", "HasCrCard", "IsActiveMember", "Complain", "Satisfaction Score", "Card Type"]
df[variables_cat] = df[variables_cat].astype("category")
secciones = [0,10,20,30,40,50,60,70,80,90,100]
labelss = ["0-10", "11-20", "21-30","31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "90+"]
df["Edades"] = pd.cut(df["Age"], secciones,labels=labelss, include_lowest=True)

#%% Primera gráfica
mostrar_churn_1 = st.checkbox("Mostrar clientes que dimitieron", value=True)
mostrar_churn_0 = st.checkbox("Mostrar clientes que NO dimitieron", value=True)

# ---- Filtrado según checkboxes ----
filtro = []

if mostrar_churn_1:
    filtro.append(1)

if mostrar_churn_0:
    filtro.append(0)

df_filtrado = df[df["Churn"].isin(filtro)]


# ---- Gráfica ----
fig = plt.figure(figsize=(4,5))
ax = sns.countplot(
    data=df_filtrado,
    x="Churn",
    palette=['#bee7e8', '#bf4342'],
    edgecolor="black",
    hue="Churn"
)
plt.title("Churn counts")
plt.legend(['No', 'Si'])

for container in ax.containers:
    ax.bar_label(container)
st.pyplot(fig)

#%% Segunda gráfica
for col, predicor in enumerate(df_filtrado.select_dtypes("category")):
    fig = plt.figure()
    sns.countplot(data=df_filtrado, x=predicor, hue="Churn", palette=['#bee7e8', '#bf4342'], edgecolor="black")
    plt.title(f"{col} distribution by Churn")
    plt.legend(["No churn", "Churn"])
    st.pyplot(fig)