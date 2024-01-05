from models.jogador import Jogador, NJogador
from models.partida import Partida, NPartida
from models.time import Time, NTime
from models.transferencia import Transferencia, NTransferencia
import pandas as pd

class View:
    def jogador_admin():
      for jogador in View.jogador_listar():
        if jogador.get_nome() == "admin": return
      View.jogador_inserir("admin", "admin", "admin", 16)  

    def jogador_inserir(nome, email, senha, idade):
        jogador = Jogador(0, nome, email, 0, senha, idade, 0)
        NJogador.inserir(jogador)
        
    def jogador_listar():
        return NJogador.listar()

    def jogador_listar_id(id):
        return NJogador.listar_id(id)

    def jogador_atualizar(id, nome, email, idTime, senha, idade, nCamisa):
        jogador = Jogador(id, nome, email, idTime, senha, idade, nCamisa)
        NJogador.atualizar(jogador)

    def jogador_excluir(id):
        jogador = Jogador(id, "", "", "", "", "", "")
        NJogador.excluir(jogador)

    def jogador_login(email, senha):
      for jogador in View.jogador_listar():
        if jogador.get_email() == email and jogador.get_senha() == senha:
          return jogador
      return None
      
    def time_inserir(nome, pontos):
        time = Time(0, nome, pontos)
        NTime.inserir(time)

    def time_listar():
        return NTime.listar()
    
    def time_listar_id(id):
        return NTime.listar_id(id)

    def time_atualizar(id, nome, pontos):
        time = Time(id, nome, pontos)
        NTime.atualizar(time)
        
    def time_excluir(id):
        time = Time(id, "", "")
        NTime.excluir(time)
    
    def partida_inserir(data, finalizado, idMandante, idVisitante, rodada, resultado):
        if idMandante == idVisitante:
            raise ValueError("Os times não podem ser iguais")
        elif finalizado == True and len(resultado.strip()) == 0:
            raise ValueError("Coloque o resultado da partida")
        else:
          for partida in View.partida_listar():
              if partida.get_rodada() == rodada:
                if idMandante == partida.get_idMandante() or idMandante == partida.get_idVisitante() or idVisitante == partida.get_idMandante() or idVisitante == partida.get_idMandante():
                    raise ValueError("O time ja jogou esta rodada")
        if finalizado:
            placar = resultado.split("x")
            mandante = View.time_listar_id(idMandante)
            visitante = View.time_listar_id(idVisitante)
            if placar[0] > placar[1]:
                nome = mandante.get_nome()
                pontos = mandante.get_pontos() + 3
                View.time_atualizar(idMandante, nome, pontos)
            elif placar[0] < placar[1]:
                nome = visitante.get_nome()
                pontos = visitante.get_pontos() + 3
                View.time_atualizar(idVisitante, nome, pontos)
            else:
                nome = mandante.get_nome()
                pontos = mandante.get_pontos() + 1
                View.time_atualizar(idMandante, nome, pontos)

                nome = visitante.get_nome()
                pontos = visitante.get_pontos() + 1
                View.time_atualizar(idVisitante, nome, pontos)

        partida = Partida(0, data, finalizado, idMandante, idVisitante, rodada, resultado)
        NPartida.inserir(partida)
    
    def partida_listar():
        return NPartida.listar()
    
    def partida_listar_id(id):
        return NPartida.listar_id(id)
    
    def partida_listar_tabela():
            partidas = View.partida_listar()
            times = View.time_listar()
            ids = []
            nmandantes = []
            nvisitantes = []
            datas = []
            rodadas = []
            finalizados = []
            resultados = []
            for obj in partidas:
              ids.append(obj.get_id())
              for time in times:
                idm = obj.get_idMandante()
                idv = obj.get_idVisitante()
                
                if View.time.listar_id(idm) == None or View.time_listar_id(idv) == None:
                    View.partida_excluir(obj.get_id())

                if time.get_id() == obj.get_idMandante():
                  nmandantes.append(time.get_nome())
                if time.get_id() == obj.get_idVisitante():
                  nvisitantes.append(time.get_nome())
              datas.append(obj.get_data())
              rodadas.append(obj.get_rodada())
              finalizados.append(obj.get_finalizado())
              resultados.append(obj.get_resultado())
            df = pd.DataFrame({
               "Id": ids,
               "Time Mandante": nmandantes,
               "Time Visitante": nvisitantes,
               "Data": datas,
               "Rodada": rodadas,
               "Finalizado": finalizados,
               "Resultado": resultados
})          
            return df
    
    def partida_atualizar(id, idMandante, idVisitante, finalizado, resultado):
        partida = Partida(id, idMandante, idVisitante, finalizado, resultado)
        NPartida.atualizar(partida)
    
    def partida_excluir(id):
        partida = View.partida_listar_id(id)
        resultado = partida.get_resultado()
        idMandante = partida.get_idMandante()
        idVisitante = partida.get_idVisitante()
        placar = resultado.split("x")
        mandante = View.time_listar_id(idMandante)
        visitante = View.time_listar_id(idVisitante)
        if placar[0] > placar[1]:
                nome = mandante.get_nome()
                pontos = mandante.get_pontos() - 3
                View.time_atualizar(idMandante, nome, pontos)
        elif placar[0] < placar[1]:
                nome = visitante.get_nome()
                pontos = visitante.get_pontos() - 3
                View.time_atualizar(idVisitante, nome, pontos)
        else:
                nome = mandante.get_nome()
                pontos = mandante.get_pontos() - 1
                View.time_atualizar(idMandante, nome, pontos)

                nome = visitante.get_nome()
                pontos = visitante.get_pontos() - 1
                View.time_atualizar(idVisitante, nome, pontos)
        partida = Partida(id, "", "", "", "","","")
        NPartida.excluir(partida)

    def partida_Visualizar(rodada):
        partidas = []
        for partida in NPartida.listar():
            if partida.get_rodada() == str(rodada):
                partidas.append(partida)
        return partidas
    
    def transferencia_inserir(idTimeEntrou, idTimeSaiu, idJogador, valor, data, NovoNCamisa, confirmada):
        transferencia = Transferencia(0, idJogador, idTimeEntrou, idTimeSaiu, valor, data, NovoNCamisa, confirmada)
        NTransferencia.inserir(transferencia)
        if confirmada:
            id = idJogador
            nome = View.jogador_listar_id(id).get_nome()
            email = View.jogador_listar_id(id).get_email()
            idTime = idTimeEntrou
            senha = View.jogador_listar_id(id).get_senha()
            idade = View.jogador_listar_id(id).get_idade()
            View.jogador_atualizar(id, nome, email, idTime, senha, idade, NovoNCamisa)
    
    def transferencia_listar():
        return NTransferencia.listar()
    
    def transferencia_listar_id(id):
        return NTransferencia.listar_id(id)
    
    def transferencia_ver_do_jogador(obj):
        transferencias = []
        for transferencia in NTransferencia.listar():
            if transferencia.get_idJogador() == obj.get_id():
                transferencias.append(transferencia)
        return transferencias
    
    def transferencia_atualizar(id, idTimeEntrou, idTimeSaiu, idJogador, valor, data, NovoNCamisa, confirmada):
        transferencia = Transferencia(id, idTimeEntrou, idTimeSaiu, idJogador, valor, data, NovoNCamisa, confirmada)
        NTransferencia.atualizar(transferencia)
        if confirmada:
            id = idJogador
            nome = View.jogador_listar_id(id).get_nome()
            email = View.jogador_listar_id(id).get_email()
            idTime = View.jogador_listar_id(id).get_idTime()
            senha = View.jogador_listar_id(id).get_senha()
            idade = View.jogador_listar_id(id).get_idade()
            View.jogador_atualizar(id, nome, email, idTime, senha, idade, NovoNCamisa)
    
    def transferencia_excluir(id):
        transferencia = Transferencia(id, "", "", "", "", "", "", "")
        NTransferencia.excluir(transferencia)
