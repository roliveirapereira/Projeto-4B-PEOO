import streamlit as st
from views import View
import pandas as pd
import time

class VisualizarTransferenciasUI:
    def main():
        st.header("Visualizar Minhas Transferências")
        tab1, tab2 = st.tabs(["Listar", "Pedir transferência"])

        with tab1: VisualizarTransferenciasUI.listar()
        with tab2: VisualizarTransferenciasUI.pedir_transferencia()
    
    def listar():
        op =View.jogador_listar_id(st.session_state["jogador_id"])
        transferencias = View.transferencia_ver_do_jogador(op)
        if len(transferencias) == 0:
            st.write("Nenhuma transferencia até agora :(")
        else:
            dic = []
            for obj in transferencias: 
                dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True, width=1000)

    def pedir_transferencia():
      try:
        op = View.jogador_listar_id(st.session_state["jogador_id"])
        times = View.time_listar()
        id = op.get_id()
        idTimeEntrou = (st.selectbox("Time que vai entrar", times)).get_id()
        idTimeSaiu = op.get_idTime()
        if idTimeEntrou == idTimeSaiu:
            raise ValueError()
        valor = st.number_input("Valor", min_value=0.00)
        data = st.date_input("Data")
        novoNcamisa = st.number_input("Novo numero da camisa", min_value=1, max_value=99)
        if st.button("Pedir transferência"):
          View.transferencia_inserir(idTimeEntrou, idTimeSaiu, id, valor, data, novoNcamisa, False)
          st.success("Solicitação feita com sucesso")
          time.sleep(2)
          st.rerun()
      except ValueError:
         st.error("O time que você vai entrar não pode ser igual ao novo")