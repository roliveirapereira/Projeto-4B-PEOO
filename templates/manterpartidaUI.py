import streamlit as st
from views import View
import pandas as pd
import datetime
import time

class ManterPartidaUI:
    def main():
        st.header("Manter Partidas")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1: ManterPartidaUI.listar()
        with tab2: ManterPartidaUI.inserir()
        with tab3: ManterPartidaUI.atualizar()
        with tab4: ManterPartidaUI.excluir()    
    def listar():
        partidas = View.partida_listar()
        if len(partidas) == 0:
            st.write("Nenhuma partida cadastrada :(")
        else:
            st.dataframe(View.partida_listar_tabela(), hide_index=True)
    
    def inserir():
        times = View.time_listar()
        idMandante = (st.selectbox("Time Mandante", times)).get_id()
        idVisitante = (st.selectbox("Time Visitante", times)).get_id()
        data = st.date_input("Data")
        rodada = st.text_input("Rodada referente a partida")
        finalizado = st.checkbox("Finalizada")
        resultado = st.text_input("Resultado (0x0)")
        if st.button("Inserir"):
            View.partida_inserir(data, finalizado, idMandante, idVisitante, rodada, resultado)
            st.success("Partida inserida com sucesso")
            time.sleep(2)
            st.rerun()
        
    def atualizar():
        partidas = View.partida_listar()
        times = View.time_listar()
        if len(partidas) == 0:
            st.write("Ainda não tem nenhuma partida cadastrada :(")
        else:
            op = st.selectbox("Atualizar partidas", partidas)
            idMandante = (st.selectbox("Novo time Mandante", times)).get_id()
            idVisitante = (st.selectbox("Novo time Visitante", times)).get_id()
            data = st.date_input("Nova data")
            rodada = st.text_input("Nova rodada referente a partida")
            finalizado = st.checkbox("Finalizada:")
            resultado = st.text_input("Resultado (0x0):")
            if st.button("Atualizar"):
                View.partida_atualizar(data, finalizado, idMandante, idVisitante, rodada, resultado)

    def excluir():
        partidas = View.partida_listar()
        if len(partidas) == 0:
            st.write("Ainda não tem nenhuma partida cadastrada :(")
        else:
            op = st.selectbox("Excluir partidas", partidas)
            if st.button("Excluir"):
                id = op.get_id()
                resultado = op.get_resultado()
                View.partida_excluir(id)
                st.success("Partida excluída com sucesso")
                time.sleep(2)
                st.rerun()
