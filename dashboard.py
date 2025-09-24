import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

#dados

turnos = ["1º TURNO", "2º TURNO", "3º TURNO"]
producao = [345, 320, 300]

total_retrabalhados = 29
total_defeitos = 47
velocidade = 70
estimativa = 620
perda = 10

defeitos = {
    "DECOTRIM ARRANHADO": 5,
    "BOLSTER DEFORMADO": 4,
    "CAPA DE COLUNA ARRANHADA": 3,
    "AUSÊNCIA DE DUTO DE AR ": 1,
    "ANTENA DESCONECTADA": 1,
    "PORTA-LUVAS ARRANHADO": 2
}

scraps = {"DECOTRIM ARRANHADO": 4}

#steamliT

st.set_page_config(page_title="DASHBOARD PRODUÇÃO", layout="wide")

st.title("DASHBOARD DE PRODUÇÃO INDUSTRIAL - 20/09/2025")

#gráfico

fig_pizza = go.Figure(data=[go.Pie(
    labels=turnos,
    values=producao,
    hole=0.3,
    pull=[0.05, 0.05, 0.05],
    marker=dict(colors=["#60e6f8", "#061994", "#0f7c88"])
)])
fig_pizza.update_layout(
    title="PRODUÇÃO POR TURNO",
    paper_bgcolor="black",
    font=dict(color="white", size=25)
)

#defeitos

fig_defeitos = px.bar(
    x=list(defeitos.values()),
    y=list(defeitos.keys()),
    orientation="h",
    color=list(defeitos.values()),
    color_continuous_scale=["#d6cc6c", "#8a2c34"],
    title="DEFEITOS ENCONTRADOS NA INSPEÇÃO FINAL"
)
fig_defeitos.update_layout(
    paper_bgcolor="black",
    plot_bgcolor="black",
    font=dict(color="white", size=14)
)

#Scraps

fig_scraps = px.bar(
    x=list(scraps.keys()),
    y=list(scraps.values()),
    color=list(scraps.values()),
    color_continuous_scale=["black", "darkred"],
    title="SCRAPS"
)
fig_scraps.update_layout(
    paper_bgcolor="black",
    plot_bgcolor="black",
    font=dict(color="white", size=14)
)

#principais

col1, col2, col3 = st.columns(3)
col1.metric("TOTAL PRODUZIDO", sum(producao))
col2.metric("RETRABALHOS", total_retrabalhados)
col3.metric("DEFEITOS PEGOS NA INSPEÇÃO FINAL", total_defeitos)

col4, col5, col6 = st.columns(3)
col4.metric("VELOCIDADE DO CARROSSEL", velocidade)
col5.metric("ESTIMATIVA DE PRODUÇÃO PARA SÁBADO (apenas 1º e 2º turno)", estimativa)
col6.metric("PERDA DE CARROS POR HORA", perda)

#visualização

st.plotly_chart(fig_pizza, use_container_width=True)
st.plotly_chart(fig_defeitos, use_container_width=True)
st.plotly_chart(fig_scraps, use_container_width=True)