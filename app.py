import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

churn_0_check = True
churn_1_check = True

# Leer los datos del archivo CSV
df = pd.read_csv("Database/Customer-Churn-Records.csv")

#%%% Intro
"""
# Análisis de clientes bancarios que dimitieron

Este dataset fue obtenido de Kaggel: https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn/data

Ya realicé el EDA de este proyecto, por lo que recomiendo vayan al repositorio donde podrán ver todos los archivos: https://github.com/ricardo4lvarez/vehicles_app.git
"""

"""
Voy a comenzar identificando cuántos de los usuarios han dimitido y cuántos no.
"""

#%% Limpieza
df.drop(columns=["RowNumber", "CustomerId", "Surname"], axis=1, inplace=True)
df.rename(columns={"Exited":"Churn"}, inplace=True)
variables_cat = ["Tenure", "Geography", "Gender", "NumOfProducts", "HasCrCard", "IsActiveMember", "Complain", "Satisfaction Score", "Card Type"]
df[variables_cat] = df[variables_cat].astype("category")
secciones = [0,10,20,30,40,50,60,70,80,90,100]
labelss = ["0-10", "11-20", "21-30","31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "90+"]
df["Edades"] = pd.cut(df["Age"], secciones,labels=labelss, include_lowest=True)

#%% Filtro con cehckboxes
mostrar_churn_1 = st.checkbox("Mostrar clientes que dimitieron", value=True)
mostrar_churn_0 = st.checkbox("Mostrar clientes que NO dimitieron", value=True)

filtro = []

if mostrar_churn_1:
    churn_1_check = True
    filtro.append(1)
else:
    churn_1_check = False

if mostrar_churn_0:
    churn_0_check = True
    filtro.append(0)
else:
    churn_0_check = False

df_filtrado = df[df["Churn"].isin(filtro)]

#%%Primera gáfica
fig = plt.figure()
ax = sns.countplot(
    data=df_filtrado,
    x="Churn",
    palette=['#bee7e8', '#bf4342'],
    edgecolor="black",
    hue="Churn"
)

plt.title("Churn counts")

if churn_1_check & churn_0_check:
    plt.legend(['No', 'Yes'])
elif not churn_0_check & churn_1_check:
    plt.legend(['No'])
elif not churn_1_check & churn_0_check:
    plt.legend(['Yes'])

for container in ax.containers:
    ax.bar_label(container)
st.pyplot(fig)

"""
# Análisis univariable
Ahora vamos a iniciar con un análisis univariable de las columnas categóricas respecto a los usuarios que dimitieron y los que no 

NOTA: 1 significa que dimitieron, 0 significa que siguen usando el servicio.
"""

#%% Segunda gráfica
for col, predicor in enumerate(df_filtrado.select_dtypes("category")):
    fig = plt.figure()
    sns.countplot(data=df_filtrado, x=predicor, hue="Churn", palette=['#bee7e8', '#bf4342'], edgecolor="black")
    plt.title(f"{predicor} distribution by Churn")
    st.pyplot(fig)

#%% Insigths del análisis univariable
"""## Insights

- Podemos observar que el grupo de edad que más *abandona* 30 años a los 60 años.
- Los productos 3 y 4 tienen más personas que *abandonan* que usuarios activos casi en un 100%.
- Si una persona ha hecho alguna queja es probable, casi en un 100%, que va a *abandonar*.
- Las personas que viven en Alemania *abandonan* la compañía con más frecuencia.
- Las mujeres tienen a *abandonar* los servicios más que los hombres.
"""

#%%% KDA plots

"""
#Análisis univariable
Ahora vamos a iniciar con un análisis univariable de las columnas numéricas respecto a los usuarios que dimitieron y los que no 

NOTA: 1 significa que dimitieron, 0 significa que siguen usando el servicio.

"""

for i, predicor in enumerate(df_filtrado.select_dtypes("number")):
    if predicor == 'Churn':
        continue
    
    fig = plt.figure()
    sns.kdeplot(data=df_filtrado, x=predicor, hue="Churn")
    
    #Configurar la leyenda dependiendo del filtro
    if churn_1_check & churn_0_check:
        plt.legend(['No', 'Yes'])
    elif churn_1_check & churn_0_check == False:
        plt.legend(['No'])
    elif churn_1_check == False & churn_0_check:
        plt.legend(['Yes'])

    st.pyplot(fig)

"""
## Insights

- Podemos observar que el grupo de edad que más *abandona* 30 años a los 60 años.
- Los productos 3 y 4 tienen más personas que *abandonan* que usuarios activos casi en un 100%.
- Si una persona ha hecho alguna queja es probable, casi en un 100%, que va a *abandonar*.
- Las personas que viven en Alemania *abandonan* la compañía con más frecuencia.
- Las mujeres tienen a *abandonar* los servicios más que los hombres.
"""

#%% Churn vs no churn análisis

"""
# Análisis bivariable

La primer gráfica siempre va a ser la de aquellos que han dimitido y la segunda los que no.
"""

grupo1 = df[df["Churn"] == 1]
grupo2 = df[df["Churn"] == 0]

fig = plt.figure(figsize=(10,6))
ax = sns.countplot(data=grupo1, x="Gender", hue="Geography", palette="pastel", edgecolor="black")
plt.title("Churners count by Gender and Geography")
for container in ax.containers:
    ax.bar_label(container)
st.pyplot(fig)

fig = plt.figure(figsize=(10,5))
ax = sns.countplot(data=grupo2, x="Gender", hue="Geography", palette="pastel", edgecolor="black")
plt.title("NO churners count by Gender and Geography")
for container in ax.containers:
    ax.bar_label(container)
st.pyplot(fig)

"""
## Insights

- Observamos que Alemania y Francia tienen la mayor cantidad de personas que *abandonan* la compañía, sin embargo, proporcionalmente Alemania es mayor su taza de abandono, 37.2% para las mujeres y 27.8% para los hombres.
- Volvemos a apreciar que las mujeres son más propensas a *abandonar*que los hombres.
"""

#%% Análisis de correlación

