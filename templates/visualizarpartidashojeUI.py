import streamlit as st
import pandas as pd
from views import View
class VisualizarPartidasUI:
    def main():
        st.header("Visualizar Partidas")
        VisualizarPartidasUI.listar()

    def listar():
        rodada = st.number_input("Diga uma rodada", min_value=1, max_value=10)
        if st.button("Atualizar"):
           partidas = View.partida_Visualizar(rodada)
           if len(partidas) == 0:
              st.write("Nenhuma partida cadastrada :(")
           else:
               dic = []
               for obj in partidas: 
                   dic.append(obj.to_json())
               df = pd.DataFrame(dic)
               st.dataframe(df, hide_index=True, width=1000)  