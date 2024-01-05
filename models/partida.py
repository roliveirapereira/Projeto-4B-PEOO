import json
import datetime
from models.modelo import Modelo

class Partida:
  def __init__(self, id, data, finalizado, idMandante, idVisitante, rodada, resultado):
    self.__id = id
    self.__data = data
    self.__finalizado = finalizado
    self.__idMandante = idMandante
    self.__idVisitante = idVisitante
    self.__rodada = rodada
    self.__resultado = resultado

  def get_id(self): return self.__id
  def get_data(self): return self.__data
  def get_finalizado(self): return self.__finalizado
  def get_idMandante(self): return self.__idMandante
  def get_idVisitante(self): return self.__idVisitante
  def get_rodada(self): return self.__rodada
  def get_resultado(self): return self.__resultado

  def set_id(self, id): 
    if isinstance(id, int):
      self.__id = id
    else:
      raise ValueError("Id invalido")
    
  def set_data(self, data):
    if isinstance(data, datetime):
      self.__data = data
    else:
      raise ValueError("O valor informado não corresponde a uma data valida")
    
  def set_finalizado(self, finalizado):
    if finalizado == True or finalizado == False:  #não achei como que verifica valor boleano pelo isintance
      self.__finalizado = finalizado
    else:
      raise ValueError("O valor informado não corresponde a uma opção valida")
    
  def set_idMandante(self, idMandante):
    if isinstance(idMandante, int):
      self.__idMandante = idMandante
    else:
      raise ValueError("O id do time mandante não é um número inteiro")
    
  def set_idVisitante(self, idVisitante):
    if isinstance(idVisitante, int):
      self.__idVisitante = idVisitante
    else:
      raise ValueError("O id do time visitante não é um número inteiro")
  
  def set_rodada(self, rodada):
    self.__rodada = rodada
  
  def set_resultado(self, resultado):
    self.__resultado = resultado

  def __eq__(self, x):
    if self.__id == x.__id and self.__data == x.__data and self.__finalizado == x.__finalizado and self.__idMandante == x.__idMandante and self.__idVisitante == x.__idVisitante and self.__rodada == x.__rodada and self.__resultado == x.__resultado:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__finalizado} - {self.__idMandante} - {self.__idVisitante} - {self.__rodada} - {self.__resultado}"

  def to_json(self):
    return {
      'Id': self.__id,
      'Data': self.__data.strftime('%d/%m/%Y %H:%M'),
      'Finalizado': self.__finalizado,
      'Id do Time Mandante': self.__idMandante,
      'Id do Time Visitante': self.__idVisitante,
      'Rodada': self.__rodada,
      'Resultado': self.__resultado}


class NPartida(Modelo):
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("partidas.json", mode="r") as arquivo:
        partidas_json = json.load(arquivo)
        for obj in partidas_json:
          aux = Partida(
            obj["Id"],
            datetime.datetime.strptime(obj["Data"], "%d/%m/%Y %H:%M"),
            obj["Finalizado"], obj["Id do Time Mandante"], obj["Id do Time Visitante"], obj["Rodada"], obj["Resultado"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("partidas.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=Partida.to_json)