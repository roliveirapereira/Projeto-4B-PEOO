import streamlit as st
from views import View
import pandas as pd

class VisualizarJogadoresUI:
    def main():
        st.header("Visualizar Jogadores")
        VisualizarJogadoresUI.listar()
    def listar():
        jogadores = View.jogador_listar()
        if len(jogadores) == 0:
            st.write("Nenhum jogador cadastrado :(")
        else:
            dic = []
            for obj in jogadores: 
                if obj.get_nome() == "admin":
                    pass
                else:
                   dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True, width=1000)