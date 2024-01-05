from templates.manterjogadorUI import ManterJogadorUI
from templates.manterpartidaUI import ManterPartidaUI
from templates.mantertimeUI import ManterTimeUI
from templates.mantertransferenciaUI import ManterTransferenciaUI
from templates.visualizarpartidashojeUI import VisualizarPartidasUI
from templates.visualizartimesUI import VisualizarTimesUI
from templates.visualizarjogadoresUI import VisualizarJogadoresUI
from templates.visualizartransferenciasUI import VisualizarTransferenciasUI
from templates.loginUI import LoginUI
from templates.abrircontaUI import AbrirContaUI
from templates.editarperfilUI import EditarPerfilUI
from views import View

import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login": LoginUI.main()
    if op == "Abrir Conta": AbrirContaUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Times", "Manter Jogadores", "Manter Partidas", "Manter Transferências", "Editar Perfil"])
    if op == "Manter Times": ManterTimeUI.main()
    if op == "Manter Jogadores": ManterJogadorUI.main()
    if op == "Manter Partidas": ManterPartidaUI.main()
    if op == "Manter Transferências": ManterTransferenciaUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()

  def menu_jogador():
    op = st.sidebar.selectbox("Menu", ["Visualizar partidas de hoje", "Visualizar Times", "Visualizar Jogadores", "Visualizar Suas Transferências", "Editar Perfil"])
    if op == "Visualizar partidas de hoje": VisualizarPartidasUI.main()
    if op == "Visualizar Times": VisualizarTimesUI.main()
    if op == "Visualizar Jogadores": VisualizarJogadoresUI.main()
    if op == "Visualizar Suas Transferências": VisualizarTransferenciasUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()

  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["jogador_id"]
      del st.session_state["jogador_nome"]
      st.rerun()

  def sidebar():
    if "jogador_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["jogador_nome"])
      if st.session_state["jogador_nome"] == "admin": IndexUI.menu_admin()
      else: IndexUI.menu_jogador()
      IndexUI.btn_logout()  

  def main():
    View.jogador_admin()
    IndexUI.sidebar()

IndexUI.main()


