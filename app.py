import streamlit as st
import pandas as pd

# Autenticação
st.set_page_config(page_title="Sistema Termos Delegatários", layout="wide")

st.sidebar.title("Login")
usuario = st.sidebar.text_input("Usuário")
senha = st.sidebar.text_input("Senha", type="password")

if usuario == "COGEX" and senha == "CGX":
    st.sidebar.success("Autenticado com sucesso!")

    # Links das planilhas
    links = {
        "Página 1": "https://docs.google.com/spreadsheets/d/e/2PACX-1vToDzpkCDB6KRyyh15H2nySmXaXmlGWWJkeaLhzQMUcTUbJUt2ExHVo35haTscfpfpdwFR_tH9vFEbs/pub?gid=2101415271&single=true&output=csv",
        "Página 2": "https://docs.google.com/spreadsheets/d/e/2PACX-1vToDzpkCDB6KRyyh15H2nySmXaXmlGWWJkeaLhzQMUcTUbJUt2ExHVo35haTscfpfpdwFR_tH9vFEbs/pub?gid=699612606&single=true&output=csv",
        "Página 3": "https://docs.google.com/spreadsheets/d/e/2PACX-1vToDzpkCDB6KRyyh15H2nySmXaXmlGWWJkeaLhzQMUcTUbJUt2ExHVo35haTscfpfpdwFR_tH9vFEbs/pub?gid=789251925&single=true&output=csv",
        "Página 4": "https://docs.google.com/spreadsheets/d/e/2PACX-1vToDzpkCDB6KRyyh15H2nySmXaXmlGWWJkeaLhzQMUcTUbJUt2ExHVo35haTscfpfpdwFR_tH9vFEbs/pub?gid=1236835293&single=true&output=csv"
    }

    abas = st.tabs(["Página 1", "Página 2", "Página 3", "Página 4"])

    textos_compilados = ""

    for idx, (pagina, link) in enumerate(links.items()):
        with abas[idx]:
            st.subheader(pagina)
            df = pd.read_csv(link)
            dados = {}
            for index, row in df.iterrows():
                dados[row['Campo']] = st.text_input(f"{row['Campo']}", key=f"pg{idx+1}_{index}")

            if pagina == "Página 1":
                texto = f"""
ESTADO DO MARANHÃO
PODER JUDICIÁRIO
CORREGEDORIA GERAL DE JUSTIÇA

TERMO DE POSSE E INVESTIDURA DE {dados.get('Nome do investido', '________________')} 
NA TITULARIDADE DOS SERVIÇOS NOTARIAIS E REGISTRAIS DA SERVENTIA EXTRAJUDICIAL DO {dados.get('Nome da serventia', '________________')}.

Aos {dados.get('Data do termo', '________________')}, nesta cidade de São Luís, capital do Estado do Maranhão, no prédio sede da Corregedoria Geral de Justiça, presente o Excelentíssimo Desembargador {dados.get('Nome do Desembargador Corregedor', '________________')}, Corregedor-Geral da Justiça, compareceu o(a) Senhor(a) {dados.get('Nome do investido', '________________')}, para tomar posse e ser investido(a) na titularidade da serventia extrajudicial do {dados.get('Nome da serventia', '________________')}, delegação outorgada em razão de aprovação em concurso público de ingresso regido pelo Edital {dados.get('Número do Edital', '________________')}, por meio do Ato n.º {dados.get('Número do Ato', '________________')}, assinado pelo Desembargador {dados.get('Nome do presidente do TJ', '________________')}, Presidente do Tribunal de Justiça do Maranhão, datado de {dados.get('Data do Ato', '________________')}, publicado no DJe do dia {dados.get('Data da publicação', '________________')}. Dispensada nova apresentação dos documentos exigidos pelos arts. 65 e 66 da Resolução nº 28/2010-TJMA. Deferida a posse pelo Excelentíssimo Corregedor-Geral da Justiça, nos termos do art. 67 da Resolução nº 28/2010-TJMA.

Eu, {dados.get('Nome do Diretor da Secretaria', '________________')}, Diretor da Secretaria da Corregedoria, lavrei o presente termo, que vai por mim e por todos assinado.

Desembargador {dados.get('Nome do Desembargador Corregedor', '________________')}
Corregedor-Geral da Justiça

{dados.get('Nome do investido', '________________')}
Delegatário(a)
"""

            elif pagina == "Página 2":
                texto = f"""
ESTADO DO MARANHÃO
PODER JUDICIÁRIO

FORMULÁRIO CADASTRAL DE TABELIÃO E/OU REGISTRADOR

Nome: {dados.get('Nome completo', '________________')}
Filiação: {dados.get('Filiação', '________________')}
CPF: {dados.get('CPF', '________________')}
RG: {dados.get('RG', '________________')}
Data de emissão do RG: {dados.get('Data de emissão RG', '________________')}
Órgão Emissor do RG: {dados.get('Órgão Emissor RG', '________________')}
Título de Eleitor: {dados.get('Título de eleitor', '________________')}
Zona e Seção: {dados.get('Zona e Seção', '________________')}
Endereço: {dados.get('Endereço', '________________')}
Telefone: {dados.get('Telefone', '________________')}
E-mail: {dados.get('E-mail', '________________')}
Estado Civil: {dados.get('Estado Civil', '________________')}
Nome do Cônjuge: {dados.get('Nome do Cônjuge', '________________')}
Escolaridade: {dados.get('Escolaridade', '________________')}
Últimas funções profissionais: {dados.get('Histórico profissional', '________________')}

Declaro que residirei no município de {dados.get('Declaração de residência', '________________')}, onde exercerei minhas funções.

Local e Data: ________________________________

Assinatura do Tabelião e/ou Registrador
"""

            elif pagina == "Página 3":
                opcao = st.radio("Possui bens a declarar?", ("NÃO POSSUO BENS A DECLARAR.", "POSSUO BENS A DECLARAR, CONFORME SEGUE ABAIXO."), key=f"opcao_pg3")
                texto = f"""
ESTADO DO MARANHÃO
PODER JUDICIÁRIO

DECLARAÇÃO DE BENS (ART. 13 DA LEI FEDERAL Nº 8.429/1992)

Eu, {dados.get('Nome do declarante', '________________')},
CPF nº {dados.get('CPF', '________________')}, RG nº {dados.get('RG', '________________')},
DECLARO, NESTA DATA, QUE:

({opcao})

Local e Data: {dados.get('Local e data', '________________')}

Assinatura do Candidato(a)
"""

            elif pagina == "Página 4":
                texto = f"""
ESTADO DO MARANHÃO
PODER JUDICIÁRIO
CORREGEDORIA GERAL DE JUSTIÇA

DECLARAÇÃO DE NÃO ACUMULAÇÃO DE CARGO, EMPREGO OU FUNÇÃO PÚBLICA

Eu, {dados.get('Nome completo', '________________')}, CPF nº {dados.get('CPF', '________________')},
DECLARO, sob as penas da lei e para atendimento à conclusão do concurso público de ingresso e remoção na atividade notarial e registral do Estado do Maranhão (Edital 01/2016-TJMA), que não percebo proventos de aposentadoria decorrentes do artigo 40, ou dos artigos 42 e 142 da Constituição Federal, salvo as hipóteses previstas no § 10º do artigo 37 do mesmo diploma legal, bem como que não exerço cargo incompatível com aquele para o qual pretendo delegação, nos termos do artigo 25 da Lei Federal nº 8.935/1994, nem a titularidade de serventia extrajudicial em outro Estado da Federação, ressalvado que, se o exerço, dele me exonerarei antes de entrar em exercício ou, se aposentado, renunciarei aos respectivos proventos, comprovando tal situação no prazo máximo de 30 (trinta) dias a contar da posse.

Local e Data: {dados.get('Local e data', '________________')}

Assinatura do Candidato(a)
"""

            if st.button(f"Finalizar {pagina}"):
                st.markdown(f"""<div style='white-space: pre-wrap; font-family: Arial; font-size: 16px;'>{texto}</div>""", unsafe_allow_html=True)
                st.success(f"{pagina} pronta para impressão!")

            textos_compilados += texto + "\n\n"

    if st.sidebar.button("Gerar Documento Completo"):
        st.markdown(f"""<div style='white-space: pre-wrap; font-family: Arial; font-size: 16px;'>{textos_compilados}</div>""", unsafe_allow_html=True)
        st.sidebar.success("Documento completo pronto para impressão!")

else:
    st.sidebar.warning("Aguardando autenticação...")
