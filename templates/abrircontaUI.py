import streamlit as st
from views import View
import time

class AbrirContaUI:
  def main():
    st.header("Abrir Conta no Sistema")
    AbrirContaUI.inserir()
  
  def inserir():
    nome = st.text_input("Informe o nome")
    idade = st.number_input("Informe a idade", min_value=16, max_value=99)
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      View.jogador_inserir(nome, email, senha, idade)
      st.success("Conta criada com sucesso")
      time.sleep(2)
      st.rerun()