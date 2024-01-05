import streamlit as st
from views import View
import pandas as pd
import time

class ManterJogadorUI:
    def main():
        st.header("Cadastro de jogadores")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1: ManterJogadorUI.listar()
        with tab2: ManterJogadorUI.inserir()
        with tab3: ManterJogadorUI.atualizar()
        with tab4: ManterJogadorUI.excluir()    
    
    def listar():
        jogadores = View.jogador_listar()
        if len(jogadores) == 0:
          st.write("Nenhum jogador cadastrado :(")
        else:
            dic = []
            for obj in jogadores: dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True, width=1000)


    def inserir():
        nome = st.text_input("Nome do jogador")
        idade = st.number_input("Idade do jogador", min_value=16, max_value=99)
        email = st.text_input('E-mail')
        senha = st.text_input("Senha")
        if st.button("Inserir"):
            View.jogador_inserir(nome, email, senha, idade)
            st.success("Jogador inserido com sucesso :D")
            time.sleep(2)
            st.rerun()

    def atualizar():
        jogadores = View.jogador_listar()
        if len(jogadores) == 0:
            st.write("Ainda não tem nenhum jogador cadastrado :(")
        else:
            op = st.selectbox("Atualizar jogadores", jogadores)
            nome = st.text_input("Novo nome", op.get_nome())
            idade = st.number_input("Nova idade", 16, 99, op.get_idade())
            email = st.text_input("Novo e-mail", op.get_email())
            senha = st.text_input("Nova senha", op.get_senha())
            if st.button("Atualizar"):
                id = op.get_id()
                idTime = op.get_idTime()
                nCamisa = op.get_nCamisa()
                View.jogador_atualizar(id, nome, email, idTime, senha, idade, nCamisa)
                st.success("Jogador excluído com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        jogadores = View.jogador_listar()
        if len(jogadores) == 0:
            st.write("Ainda não tem nenhum jogador cadastrado :(")
        else:
            op = st.selectbox("Excluir jogadores", jogadores)
            if st.button("Excluir"):
                id = op.get_id()
                View.jogador_excluir(id)
                st.success("Jogador excluído com sucesso")
                time.sleep(2)
                st.rerun()