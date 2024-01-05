import streamlit as st
from views import View
import pandas as pd

class VisualizarTimesUI:
    def main():
        st.header("Visualizar times")
        VisualizarTimesUI.listar()

    def listar():
        times = View.time_listar()
        if len(times) == 0:
            st.write("Nenhum time cadastrado :(")
        else:
            dic = []
            for obj in times: 
                dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True, width=1000)