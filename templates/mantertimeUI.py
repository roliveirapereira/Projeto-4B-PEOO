import streamlit as st
from views import View
import time
import pandas as pd
class ManterTimeUI:
    def main():
        st.header("Cadastro de times")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1: ManterTimeUI.listar()
        with tab2: ManterTimeUI.inserir()
        with tab3: ManterTimeUI.atualizar()
        with tab4: ManterTimeUI.excluir()    
    
    def listar():
        times = View.time_listar()
        if len(times) == 0:
          st.write("Nenhum time cadastrado :(")
        else:
            dic = []
            for obj in times: dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True, width=1000)

    def inserir():
        nome = st.text_input("Nome do time")
        if st.button("Inserir"):
            View.time_inserir(nome, 0)
            st.success("Time inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        times = View.time_listar()
        if len(times) == 0:
            st.write("Ainda não tem nenhum time cadastrado :(")
        else:
            op = st.selectbox("Atualizar times", times)
            nome = st.text_input("Novo nome", op.get_nome())
            if st.button("Atualizar"):
                id = op.get_id()
                pontos = op.get_pontos()
                View.time_atualizar(id, nome, pontos)
                st.success("Time atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        times = View.time_listar()
        if len(times) == 0:
            st.write("Ainda não tem nenhum time cadastrado :(")
        else:
            op = st.selectbox("Excluir times", times)
            if st.button("Excluir"):
                id = op.get_id()
                View.time_excluir(id)
                st.success("time excluído com sucesso")
                time.sleep(2)
                st.rerun()
