import streamlit as st
from views import View
import time
import pandas as pd

class ManterTransferenciaUI:
    def main():
        st.header("Cadastro de transferencias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1: ManterTransferenciaUI.listar()
        with tab2: ManterTransferenciaUI.inserir()
        with tab3: ManterTransferenciaUI.atualizar()
        with tab4: ManterTransferenciaUI.excluir()    
    
    def listar():
        transferencias = View.transferencia_listar()
        if len(transferencias) == 0:
          st.write("Nenhum Transferencia cadastrado :(")
        else:
            dic = []
            for obj in transferencias: dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True, width=1000)

    def inserir():
        jogadores = View.jogador_listar()
        times = View.time_listar()
        ObjJogador = st.selectbox("Selecione o jogador", jogadores)
        idJogador = ObjJogador.get_id()
        ObjTimeEntrou = st.selectbox("Selecione o novo time", times)
        idTimeEntrou = ObjTimeEntrou.get_id()
        idTimeSaiu = ObjJogador.get_idTime()
        valor = st.number_input("Valor da transferencia")
        data = st.date_input("Data")
        novoNCamisa = st.number_input("Novo numero da camisa", min_value=1, max_value=99)
        confirmada = st.checkbox("Confirmada?")
        if st.button("Inserir"):
            View.transferencia_inserir(idTimeEntrou, idTimeSaiu, idJogador, valor, data, novoNCamisa, confirmada)
            st.success("Transferencia inserida com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        transferencias = View.transferencia_listar()
        if len(transferencias) == 0:
            st.write("Ainda não tem nenhum Transferencia cadastrado :(")
        else:
            op = st.selectbox("Atualizar transferencias", transferencias)
            id = op.get_id()
            jogadores = View.jogador_listar()
            ObjJogador = View.jogador_listar_id(id)
            times = View.time_listar()
            idJogador = st.selectbox("Selecione o novo jogador", jogadores)
            idTimeEntrou = st.selectbox("Selecione o novo time atualizado", times)
            idTimeSaiu = ObjJogador.get_idTime()
            valor = st.number_input("Novo valor da transferencia")
            data = st.date_input("Nova Data")
            novoNCamisa = st.number_input("Novo numero da camisa:", min_value=1, max_value=99)
            confirmada = st.checkbox("Ja confirmada?")
            if st.button("Atualizar"):
               View.transferencia_atualizar(id, idTimeEntrou, idTimeSaiu, idJogador, valor, data, novoNCamisa, confirmada)
               time.sleep(2)
               st.rerun()

    def excluir():
        transferencias = View.transferencia_listar()
        if len(transferencias) == 0:
            st.write("Ainda não tem nenhuma Transferencia cadastrada :(")
        else:
            op = st.selectbox("Excluir transferencias", transferencias)
            if st.button("Excluir"):
                id = op.get_id()
                View.transferencia_excluir(id)
                st.success("Transferencia excluído com sucesso")
                time.sleep(2)
                st.rerun()
      