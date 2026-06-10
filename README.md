# Churn App
Proyecto de sprint 7 de TripleTen

Este proyecto consiste en el desarrollo de una aplicación web interactiva para el análisis del abandono de clientes (Customer Churn) en una compañía telefónica.

El objetivo principal es identificar patrones de comportamiento que expliquen por qué algunos clientes cancelan el servicio mientras otros permanecen activos, permitiendo así generar insights estratégicos orientados a la retención de clientes.

La aplicación está desplegada y puede visualizarse en el siguiente enlace: https://vehicles-app-2fst.onrender.com

## Stack Tecnológico
- Python 3
- Pandas – Manipulación y limpieza de datos
- NumPy – Operaciones numéricas
- Plotly / Matplotlib – Visualización de datos
- Streamlit (o framework usado en app.py)
- Jupyter Notebook – Análisis exploratorio
- Render – Despliegue web
- Git & GitHub – Control de versiones


## Estructura del proyecto
```
churn_app/
│
├── Database/
│   └── Dataset original
│
├── Notebooks/
│   └── Análisis exploratorio (EDA)
│
├── app.py
├── requirements.txt
└── README.md
```

## El proyecto se desarrolló siguiendo las siguientes etapas:

### Exploración de Datos (EDA)

- Identificación de valores nulos
- Análisis de variables categóricas y numéricas
- Distribución de churn
- Detección de correlaciones
- Análisis por segmentos

### Limpieza y Transformación

- Conversión de tipos de datos
- Manejo de valores faltantes
- Estandarización de variables categóricas
- Creación de métricas derivadas

### Visualización

- Se implementaron gráficos interactivos que permiten:
- Comparar churn por tipo de contrato
- Analizar churn por tiempo de permanencia
- Evaluar impacto del cargo mensual
- Comparar clientes activos vs. inactivos

### Implementación Web

La aplicación permite:

- Filtrar información
- Visualizar métricas clave
- Analizar tendencias
- Explorar datos dinámicamente

## Principales Insigths

Personas que más abandonan en proporción:

- Mujeres.
- Gente de 51 a 60 años (seguidos de gente entre 41 a 50 años).
- Alemanes.
- Los números de productos 3 y 4 independientemente del género y región. Es seguido por el 1.
- Casi el 100% de la gente que emitió una queja.

Personas que menos abandonan en proporción:

- Hombres.
- Gente de entre 31 y 40 años (seguidos de 21 a 30 años).
- Franceses.
- El número de producto que menos abandonan es el 2.
- Las personas activas tienden a abandonar menos.
