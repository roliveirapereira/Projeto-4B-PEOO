import streamlit as st
from views import View

class EditarPerfilUI:
    def main():
        st.header("Atualizar perfil")
        EditarPerfilUI.atualizar()

    def atualizar():
        op = View.jogador_listar_id(st.session_state["jogador_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        idade = st.number_input("Informe a nova idade", op.get_idade())
        novoNcamisa = st.text_input("Informe o novo numero", op.get_nCamisa())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        senha = st.text_input("Informe a nova senha")
        idTime = op.get_idTime()
        if st.button("Atualizar"):
            id = op.get_id()
            View.jogador_atualizar(id, nome, email, idTime, senha, idade, novoNcamisa)
            st.success("Perfil atualizado com sucesso")