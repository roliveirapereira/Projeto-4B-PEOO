import streamlit as st
import time
from views import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        LoginUI.entrar()
    
    def entrar():
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha")
        if st.button("Login"):
          jogador = View.jogador_login(email, senha) 
          if jogador is not None:
            st.success("Login realizado com sucesso")
            st.success("Bem-vindo(a), " + jogador.get_nome())
            st.session_state["jogador_id"] = jogador.get_id()
            st.session_state["jogador_nome"] = jogador.get_nome()
            time.sleep(2)
            st.rerun() 
          else:
            st.error("Usuário ou senha inválido(s)")
            time.sleep(2)
            st.rerun()      