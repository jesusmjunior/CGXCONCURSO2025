import streamlit as st
import pandas as pd

st.set_page_config(page_title="Termo de Investidura - Página 1", layout="wide")

st.sidebar.title("Login")
usuario = st.sidebar.text_input("Usuário")
senha = st.sidebar.text_input("Senha", type="password")

if usuario == "COGEX" and senha == "CGX":
    st.sidebar.success("Autenticado!")

    st.title("Página 1 - TERMO DE POSSE E INVESTIDURA")

    # Carregar dados
    link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vToDzpkCDB6KRyyh15H2nySmXaXmlGWWJkeaLhzQMUcTUbJUt2ExHVo35haTscfpfpdwFR_tH9vFEbs/pub?gid=2101415271&single=true&output=csv"
    df = pd.read_csv(link)

    # Captura de dados mutáveis inline
    dados = {}
    for index, row in df.iterrows():
        opcoes = [str(valor) for valor in df[row['Campo']].dropna().unique() if valor != '']
        col1, col2 = st.columns([3, 1])
        with col1:
            if opcoes:
                dados[row['Campo']] = st.selectbox(f"{row['Campo']}", options=opcoes, key=f"pg1_{index}")
            else:
                dados[row['Campo']] = st.text_input(f"{row['Campo']}", key=f"pg1_{index}")
        with col2:
            if st.checkbox(f"Manual", key=f"manual_{index}"):
                dados[row['Campo']] = st.text_input(f"Digite {row['Campo']}", key=f"input_{index}")

    # Montar texto
    texto = f"""
ESTADO DO MARANHÃO
PODER JUDICIÁRIO
CORREGEDORIA GERAL DE JUSTIÇA

TERMO DE POSSE E INVESTIDURA DE {dados.get('Nome do investido', '________________')} 
NA TITULARIDADE DOS SERVIÇOS NOTARIAIS E REGISTRAIS DA SERVENTIA EXTRAJUDICIAL DO {dados.get('Nome da serventia', '________________')}.

Aos {dados.get('Data do termo', '________________')}, nesta cidade de São Luís, capital do Estado do Maranhão, no prédio sede da Corregedoria Geral de Justiça, presente o Excelentíssimo Desembargador {dados.get('Nome do Desembargador Corregedor', '________________')}, Corregedor-Geral da Justiça, compareceu o(a) Senhor(a) {dados.get('Nome do investido', '________________')}, para tomar posse e ser investido(a) na titularidade da serventia extrajudicial do {dados.get('Nome da serventia', '________________')}, delegação outorgada em razão de aprovação em concurso público regido pelo Edital {dados.get('Número do Edital', '________________')}, por meio do Ato n.º {dados.get('Número do Ato', '________________')}, assinado pelo Desembargador {dados.get('Nome do presidente do TJ', '________________')}, datado de {dados.get('Data do Ato', '________________')}, publicado no DJe do dia {dados.get('Data da publicação', '________________')}.

Eu, {dados.get('Nome do Diretor da Secretaria', '________________')}, Diretor da Secretaria da Corregedoria, lavrei o presente termo, que vai por mim e por todos assinado.

Desembargador {dados.get('Nome do Desembargador Corregedor', '________________')}
Corregedor-Geral da Justiça

{dados.get('Nome do investido', '________________')}
Delegatário(a)
"""

    if st.button("Finalizar Página 1"):
        st.markdown(f"""<div style='white-space: pre-wrap; font-family: Arial; font-size: 16px;'>{texto}</div>""", unsafe_allow_html=True)
        st.success("Página 1 pronta para impressão!")

else:
    st.sidebar.warning("Aguardando autenticação...")
