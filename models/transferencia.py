import json
from models.modelo import Modelo
import datetime

class Transferencia:
  def __init__(self, id, idJogador, idTimeEntrou, idTimeSaiu, valor, data, novoNCamisa, confirmada):
    self.__id = id
    self.__idJogador = idJogador
    self.__idTimeEntrou = idTimeEntrou
    self.__idTimeSaiu = idTimeSaiu
    self.__valor = valor
    self.__data = data
    self.__novoNCamisa = novoNCamisa
    self.__confirmada = confirmada

  def get_id(self): return self.__id
  def get_idJogador(self): return self.__idJogador
  def get_idTimeEntrou(self): return self.__idTimeEntrou
  def get_idTimeSaiu(self): return self.__idTimeSaiu
  def get_valor(self): return self.__valor
  def get_data(self): return self.__data
  def get_novoNCamisa(self): return self.__novoNCamisa
  def get_confirmada(self): return self.__confirmada

  def set_id(self, id):
    if isinstance(id, int):
      self.__id = id
    else:
      raise ValueError("Id invalido")

  def set_idJogador(self, idJogador):
    if isinstance(idJogador, int):
      self.__idJogador = idJogador
    else:
      raise ValueError("O id do time qual o jogador saiu não é um número inteiro")

  def set_idTimeEntrou(self, idTimeEntrou):
    if isinstance(idTimeEntrou, int):
      self.__idTimeEntrou = idTimeEntrou
    else:
      raise ValueError("O id do time qual o jogador saiu não é um número inteiro")

  def set_idTimeSaiu(self, idTimeSaiu): 
    if isinstance(idTimeSaiu, int):
       self.__idTimeSaiu = idTimeSaiu
    else:
      raise ValueError("O id do time qual o jogador saiu não é um número inteiro")

  def set_valor(self, valor): 
    if isinstance(valor, float):
      self.__valor = valor
    else:
      raise ValueError("O valor informado não é válido ")

  def set_data(self, data):
    if isinstance(data, datetime):
      self.__data = data
    else:
      raise ValueError("O valor informado não corresponde a uma data valida")

  def set_novoNCamisa(self, novoNCamisa):
    if isinstance(novoNCamisa, int):
      self.__novoNCamisa = novoNCamisa
    else:
      raise ValueError("O novo numero de camisa não é valido")
  
  def set_confirmada(self, confirmada):
    self.__confirmada = confirmada

  def __eq__(self, x):
    if self.__id == x.__id and self.__idJogador == x.__idJogador and self.__idTimeEntrou == x.__idTimeEntrou and self.__idTimeSaiu == x.__idTimeSaiu and self.__valor == x.__valor and self.__data == x.__data and self.__novoNCamisa == x.__novoNCamisa and self.__confirmada == x.__confirmada:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__idJogador} - {self.__idTimeEntrou} - {self.__idTimeSaiu} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__novoNCamisa} - {self.__confirmada}"
  
  def to_json(self):
    return {
      'Id': self.__id,
      'Id do Jogador': self.__idJogador,
      'Id Time Entrou': self.__idTimeEntrou,
      'Id Time Saiu': self.__idTimeSaiu,
      'Valor': self.__valor,
      'Data': self.__data.strftime('%d/%m/%Y %H:%M'),
      'Novo n da camisa': self.__novoNCamisa,
      'Confirmada': self.__confirmada}
      

class NTransferencia(Modelo):
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("transferencias.json", mode="r") as arquivo:
        transferencias_json = json.load(arquivo)
        for obj in transferencias_json:
          aux = Transferencia(
                        obj["Id"], 
                        obj["Id do Jogador"], 
                        obj["Id Time Entrou"],
                        obj["Id Time Saiu"],
                        obj["Valor"],
                        datetime.datetime.strptime(obj["Data"], "%d/%m/%Y %H:%M"),
                        obj["Novo n da camisa"],
                        obj["Confirmada"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("transferencias.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=Transferencia.to_json)